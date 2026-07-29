from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.base import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    dataset_id = Column(
        Integer,
        ForeignKey("datasets.id"),
        nullable=False
    )

    provider = Column(
        String(50),
        nullable=False
    )

    model_name = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(20),
        default="Pending"
    )

    total_prompts = Column(
        Integer,
        default=0
    )

    completed_prompts = Column(
        Integer,
        default=0
    )

    started_at = Column(
        DateTime,
        nullable=True
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationships

    user = relationship(
        "User",
        back_populates="evaluations"
    )

    dataset = relationship(
        "Dataset",
        back_populates="evaluations"
    )

    results = relationship(
        "EvaluationResult",
        back_populates="evaluation",
        cascade="all, delete-orphan"
    )