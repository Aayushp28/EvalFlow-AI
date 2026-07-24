from fastapi import FastAPI

from app.database.init_db import init_db
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="EvalFlow AI API",
    version="1.0.0"
)

init_db()

app.include_router(
    auth_router,
    prefix="/api/v1"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to EvalFlow AI"
    }