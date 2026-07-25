import os
import uuid

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.models.dataset import Dataset
from app.models.user import User


UPLOAD_FOLDER = "uploads"

ALLOWED_FILE_TYPES = [
    "text/csv",
    "application/json"
]


def upload_dataset(
    db: Session,
    file: UploadFile,
    current_user: User
):
    # Validate file type
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only CSV and JSON files are allowed."
        )

    # Create uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Generate unique filename
    extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )

    # Save file to disk
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Get file size
    file_size = os.path.getsize(file_path)

    # Save metadata to database
    dataset = Dataset(
        filename=unique_filename,
        original_name=file.filename,
        file_type=file.content_type,
        file_size=file_size,
        owner_id=current_user.id
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return dataset

def get_user_datasets(
    db: Session,
    current_user: User
):
    return (
        db.query(Dataset)
        .filter(Dataset.owner_id == current_user.id)
        .order_by(Dataset.upload_date.desc())
        .all()
    )

def get_dataset_by_id(
    db: Session,
    dataset_id: int,
    current_user: User
):
    dataset = (
        db.query(Dataset)
        .filter(
            Dataset.id == dataset_id,
            Dataset.owner_id == current_user.id
        )
        .first()
    )

    if not dataset:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found."
        )

    return dataset

def delete_dataset(
    db: Session,
    dataset_id: int,
    current_user: User
):
    dataset = (
        db.query(Dataset)
        .filter(
            Dataset.id == dataset_id,
            Dataset.owner_id == current_user.id
        )
        .first()
    )

    if not dataset:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found."
        )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        dataset.filename
    )

    if os.path.exists(file_path):
        os.remove(file_path)

    db.delete(dataset)
    db.commit()

    return {
        "message": "Dataset deleted successfully."
    }