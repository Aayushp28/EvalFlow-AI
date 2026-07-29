from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.evaluation import (
    EvaluationCreate,
    EvaluationResponse,
)
from app.services.evaluation_service import create_evaluation

router = APIRouter(
    prefix="/evaluations",
    tags=["Evaluations"],
)


@router.post(
    "/start",
    response_model=EvaluationResponse
)
def start_evaluation(
    evaluation: EvaluationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = create_evaluation(
        db=db,
        current_user=current_user,
        dataset_id=evaluation.dataset_id,
        provider=evaluation.provider,
        model_name=evaluation.model_name,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found."
        )

    return result