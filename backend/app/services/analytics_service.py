from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.evaluation import Evaluation
from app.models.evaluation_result import EvaluationResult


class AnalyticsService:

    @staticmethod
    def get_summary(
        db: Session,
        user_id: int
    ):

        total_evaluations = (
            db.query(Evaluation)
            .filter(Evaluation.user_id == user_id)
            .count()
        )

        completed_evaluations = (
            db.query(Evaluation)
            .filter(
                Evaluation.user_id == user_id,
                Evaluation.status == "Completed"
            )
            .count()
        )

        pending_evaluations = (
            total_evaluations
            - completed_evaluations
        )

        prompt_stats = (
            db.query(
                func.sum(Evaluation.total_prompts),
                func.sum(Evaluation.completed_prompts)
            )
            .filter(Evaluation.user_id == user_id)
            .first()
        )

        total_prompts = prompt_stats[0] or 0
        completed_prompts = prompt_stats[1] or 0

        result_stats = (
            db.query(
                func.avg(EvaluationResult.latency),
                func.avg(EvaluationResult.total_tokens),
                func.sum(EvaluationResult.estimated_cost)
            )
            .join(Evaluation)
            .filter(Evaluation.user_id == user_id)
            .first()
        )

        average_latency = round(
            result_stats[0] or 0,
            3
        )

        average_tokens = round(
            result_stats[1] or 0,
            2
        )

        total_estimated_cost = round(
            result_stats[2] or 0,
            6
        )

        success_rate = 0

        if total_prompts > 0:
            success_rate = round(
                (completed_prompts / total_prompts) * 100,
                2
            )

        return {
            "total_evaluations": total_evaluations,
            "completed_evaluations": completed_evaluations,
            "pending_evaluations": pending_evaluations,
            "total_prompts": total_prompts,
            "completed_prompts": completed_prompts,
            "average_latency": average_latency,
            "average_tokens": average_tokens,
            "total_estimated_cost": total_estimated_cost,
            "success_rate": success_rate
        }