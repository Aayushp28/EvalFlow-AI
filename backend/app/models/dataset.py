from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255), nullable=False)

    original_name = Column(String(255), nullable=False)

    file_type = Column(String(50), nullable=False)

    file_size = Column(Integer, nullable=False)

    upload_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    owner = relationship(
        "User",
        back_populates="datasets"
    )

    evaluations = relationship(
    "Evaluation",
    back_populates="dataset",
    cascade="all, delete-orphan"
)