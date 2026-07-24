from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserRegister
from app.core.security import hash_password


def register_user(db: Session, user_data: UserRegister):

    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise ValueError("Email already registered")

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


def login_user(db: Session, email: str, password: str):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        raise ValueError("Invalid email or password")

    if not verify_password(password, user.password):
        raise ValueError("Invalid email or password")

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }