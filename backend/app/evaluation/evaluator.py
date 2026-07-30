import time
from pathlib import Path

import pandas as pd
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.dataset import Dataset
from app.models.evaluation import Evaluation
from app.models.evaluation_result import EvaluationResult

from app.evaluation.providers.gemini_provider import GeminiProvider
from app.evaluation.tokenizer import Tokenizer
from app.evaluation.metrics import Metrics


class Evaluator:

    PROMPT_COLUMNS = [
        "prompt",
        "question",
        "input",
        "query",
        "text"
    ]

    def __init__(self, dataset: Dataset):
        self.dataset = dataset

    def get_dataset_path(self) -> Path:
        return Path(settings.UPLOAD_FOLDER) / self.dataset.filename

    def load_prompts(self) -> list[str]:

        file_path = self.get_dataset_path()

        df = pd.read_csv(file_path)

        prompt_column = None

        for column in self.PROMPT_COLUMNS:
            if column in df.columns:
                prompt_column = column
                break

        if prompt_column is None:
            raise ValueError(
                f"No prompt column found. Expected one of {self.PROMPT_COLUMNS}"
            )

        return (
            df[prompt_column]
            .dropna()
            .astype(str)
            .tolist()
        )

    def run(
        self,
        db: Session,
        evaluation: Evaluation
    ):

        provider = GeminiProvider()
        

        prompts = self.load_prompts()

        total_prompts = len(prompts)

        print("\n===================================")
        print("Starting Evaluation")
        print("===================================")
        print(f"Total Prompts : {total_prompts}\n")

        evaluation.status = "Running"
        evaluation.completed_prompts = 0

        db.commit()

        for index, prompt in enumerate(prompts, start=1):

            print(f"[{index}/{total_prompts}] {prompt}")

            try:

                start = time.perf_counter()

                response = provider.generate(prompt)

                latency = round(
                    time.perf_counter() - start,
                    3
                )

                (
                    input_tokens,
                    output_tokens,
                    total_tokens
                ) = Tokenizer.count(
                    prompt,
                    response
                )

                estimated_cost = Metrics.estimate_cost(
                    total_tokens
                )

                # Optional LLM Judge
                score = None
                feedback = None

                result = EvaluationResult(
                    evaluation_id=evaluation.id,
                    prompt=prompt,
                    response=response,
                    latency=latency,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    total_tokens=total_tokens,
                    estimated_cost=estimated_cost,
                    score=score,
                    feedback=feedback
                )

                db.add(result)

                evaluation.completed_prompts = index

                db.commit()

                print(
                    f"✓ Completed | "
                    f"Latency: {latency}s | "
                    f"Tokens: {total_tokens}"
                )

            except Exception as e:

                db.rollback()

                print(f"✗ Error : {e}")

                result = EvaluationResult(
                    evaluation_id=evaluation.id,
                    prompt=prompt,
                    response=f"ERROR: {str(e)}",
                    latency=0,
                    input_tokens=0,
                    output_tokens=0,
                    total_tokens=0,
                    estimated_cost=0,
                    score=0,
                    feedback=str(e)
                )

                db.add(result)

                try:
                    db.commit()
                except Exception:
                    db.rollback()

        evaluation.status = "Completed"

        db.commit()

        print("\n===================================")
        print("Evaluation Completed Successfully")
        print("===================================")