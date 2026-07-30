from app.database.session import SessionLocal

# Import all models so SQLAlchemy registers relationships
from app.models.user import User
from app.models.dataset import Dataset
from app.models.evaluation import Evaluation
from app.models.evaluation_result import EvaluationResult

from app.evaluation.evaluator import Evaluator

db = SessionLocal()

dataset = db.query(Dataset).filter(Dataset.id == 3).first()

evaluator = Evaluator(dataset)

prompts = evaluator.load_prompts()

print(f"Total prompts: {len(prompts)}")

for prompt in prompts[:5]:
    print(prompt)