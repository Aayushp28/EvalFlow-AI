from app.database.session import SessionLocal

import app.models

from app.models.dataset import Dataset
from app.models.evaluation import Evaluation

from app.evaluation.evaluator import Evaluator

db = SessionLocal()

dataset = db.query(Dataset).filter(
    Dataset.id == 3
).first()

evaluation = db.query(Evaluation).filter(
    Evaluation.id == 3
).first()

evaluator = Evaluator(dataset)

evaluator.run(
    db=db,
    evaluation=evaluation
)

print("Evaluation Finished!")