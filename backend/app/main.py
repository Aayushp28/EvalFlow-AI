from app.database.init_db import *
from fastapi import FastAPI

app = FastAPI(
    title="EvalFlow AI",
    version="1.0.0",
    description="LLM Evaluation & CI/CD Automation Platform"
)

@app.get("/")
def home():
    return {
        "project": "EvalFlow AI",
        "status": "Running",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }