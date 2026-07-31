from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.evaluation import (
    EvaluationCreate,
    EvaluationResponse,
)

from app.schemas.evaluation_details import (
    EvaluationDetailsResponse,
    EvaluationInfo,
    EvaluationResultItem,
)

from app.services.evaluation_service import (
    create_evaluation,
    get_evaluation_details,
)

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


@router.get(
    "/{evaluation_id}",
    response_model=EvaluationDetailsResponse
)
def get_evaluation(
    evaluation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    data = get_evaluation_details(
        db=db,
        evaluation_id=evaluation_id,
        current_user=current_user,
    )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Evaluation not found."
        )

    evaluation = data["evaluation"]

    response = EvaluationInfo(
        id=evaluation.id,
        dataset_name=evaluation.dataset.original_name,
        provider=evaluation.provider,
        model_name=evaluation.model_name,
        status=evaluation.status,
        total_prompts=evaluation.total_prompts,
        completed_prompts=evaluation.completed_prompts,
        created_at=evaluation.created_at,
    )

    results = [
        EvaluationResultItem(
            id=result.id,
            prompt=result.prompt,
            response=result.response,
            latency=result.latency,
            input_tokens=result.input_tokens,
            output_tokens=result.output_tokens,
            total_tokens=result.total_tokens,
            estimated_cost=result.estimated_cost,
            score=result.score,
            feedback=result.feedback,
        )
        for result in data["results"]
    ]

    return {
        "evaluation": response,
        "results": results,
    }