from app.database.base import Base
from app.database.connection import engine

from app.models.user import User
from app.models.dataset import Dataset


def init_db():
    Base.metadata.create_all(bind=engine)