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