from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependency import get_db
from app.schemas.user import UserRegister, UserResponse
from app.services.auth_service import register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    try:
        return register_user(db, user)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )