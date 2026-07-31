from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.schemas.analytics import AnalyticsSummary
from app.services.analytics_service import AnalyticsService

from app.core.dependencies import get_current_user

from app.models.user import User


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get(
    "/summary",
    response_model=AnalyticsSummary
)
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return AnalyticsService.get_summary(
        db=db,
        user_id=current_user.id
    )