from app.database.base import Base
from app.database.connection import engine

from app.models.user import User
from app.models.dataset import Dataset

from app.models.evaluation import Evaluation
from app.models.evaluation_result import EvaluationResult

def init_db():
    Base.metadata.create_all(bind=engine)