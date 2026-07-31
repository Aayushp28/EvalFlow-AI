from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.evaluation_history import (
    EvaluationHistoryResponse
)

from app.services.history_service import HistoryService


router = APIRouter(
    prefix="/history",
    tags=["Evaluation History"]
)


@router.get(
    "/",
    response_model=EvaluationHistoryResponse
)
def get_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return HistoryService.get_history(
        db,
        current_user.id
    )