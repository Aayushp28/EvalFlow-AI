from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.core.dependencies import get_current_user

from app.models.user import User
from app.schemas.dataset import DatasetResponse
from app.services.dataset_service import upload_dataset

from app.services.dataset_service import (
    upload_dataset,
    get_user_datasets
)
from app.services.dataset_service import (
    upload_dataset,
    get_user_datasets,
    get_dataset_by_id
)
from app.services.dataset_service import (
    upload_dataset,
    get_user_datasets,
    get_dataset_by_id,
    delete_dataset
)
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

@router.get(
    "",
    response_model=list[DatasetResponse]
)
def get_datasets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_datasets(
        db=db,
        current_user=current_user
    )

@router.get(
    "/{dataset_id}",
    response_model=DatasetResponse
)
def get_dataset(
    dataset_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_dataset_by_id(
        db=db,
        dataset_id=dataset_id,
        current_user=current_user
    )

@router.delete("/{dataset_id}")
def remove_dataset(
    dataset_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_dataset(
        db=db,
        dataset_id=dataset_id,
        current_user=current_user
    )