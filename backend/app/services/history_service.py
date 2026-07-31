from sqlalchemy.orm import Session

from app.models.evaluation import Evaluation


class HistoryService:

    @staticmethod
    def get_history(
        db: Session,
        user_id: int
    ):

        evaluations = (
            db.query(Evaluation)
            .filter(Evaluation.user_id == user_id)
            .order_by(Evaluation.created_at.desc())
            .all()
        )

        history = []

        for evaluation in evaluations:

            history.append(
                {
                    "id": evaluation.id,
                    "dataset_name": evaluation.dataset.original_name,
                    "provider": evaluation.provider,
                    "model_name": evaluation.model_name,
                    "status": evaluation.status,
                    "total_prompts": evaluation.total_prompts,
                    "completed_prompts": evaluation.completed_prompts,
                    "created_at": evaluation.created_at
                }
            )

        return {
            "evaluations": history
        }