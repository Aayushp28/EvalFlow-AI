from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.base import Base


class EvaluationResult(Base):
    __tablename__ = "evaluation_results"

    id = Column(Integer, primary_key=True, index=True)

    evaluation_id = Column(
        Integer,
        ForeignKey("evaluations.id"),
        nullable=False
    )

    prompt = Column(
        Text,
        nullable=False
    )

    response = Column(
        Text,
        nullable=False
    )

    latency = Column(
        Float,
        default=0.0
    )

    input_tokens = Column(
        Integer,
        default=0
    )

    output_tokens = Column(
        Integer,
        default=0
    )

    total_tokens = Column(
        Integer,
        default=0
    )

    estimated_cost = Column(
        Float,
        default=0.0
    )

    score = Column(
        Float,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    evaluation = relationship(
        "Evaluation",
        back_populates="results"
    )