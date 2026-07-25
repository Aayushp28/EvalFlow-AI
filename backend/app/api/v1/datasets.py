from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.core.dependencies import get_current_user

from app.models.user import User
from app.schemas.dataset import DatasetResponse
from app.services.dataset_service import upload_dataset

router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.post(
    "/upload",
    response_model=DatasetResponse
)
def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return upload_dataset(
        db=db,
        file=file,
        current_user=current_user
    )