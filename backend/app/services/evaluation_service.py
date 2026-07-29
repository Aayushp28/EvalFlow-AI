import os
import pandas as pd

from app.core.config import settings
from sqlalchemy.orm import Session

from app.models.dataset import Dataset
from app.models.evaluation import Evaluation
from app.models.user import User


def create_evaluation(
    db: Session,
    current_user: User,
    dataset_id: int,
    provider: str,
    model_name: str,
):
    """
    Create a new evaluation for the authenticated user.
    """

    # Check dataset ownership
    dataset = (
        db.query(Dataset)
        .filter(
            Dataset.id == dataset_id,
            Dataset.owner_id == current_user.id
        )
        .first()
    )

    if not dataset:
        return None

    total_prompts, prompt_column = count_prompts(dataset)

    evaluation = Evaluation(
    user_id=current_user.id,
    dataset_id=dataset.id,
    provider=provider,
    model_name=model_name,
    status="Pending",
    total_prompts=total_prompts,
    completed_prompts=0,
)

    db.add(evaluation)
    db.commit()
    db.refresh(evaluation)

    return evaluation

def count_prompts(dataset: Dataset) -> tuple[int, str]:
    """
    Reads the uploaded dataset.

    Returns:
        total number of prompts,
        detected prompt column.
    """

    file_path = os.path.join(
        settings.UPLOAD_FOLDER,
        dataset.filename
    )
    print("=" * 60)
    print("UPLOAD_FOLDER:", settings.UPLOAD_FOLDER)
    print("DATASET FILENAME:", dataset.filename)
    print("FULL PATH:", file_path)
    print("FILE EXISTS:", os.path.exists(file_path))
    print("=" * 60)
    df = pd.read_csv(file_path)

    possible_columns = [
        "prompt",
        "question",
        "input",
        "text",
        "query"
    ]

    prompt_column = None

    for column in possible_columns:
        if column in df.columns:
            prompt_column = column
            break

    if prompt_column is None:
        raise ValueError(
            "No prompt column found in dataset."
        )

    return len(df), prompt_column