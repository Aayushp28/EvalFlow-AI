import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
    # ======================================================
    # Project Paths
    # ======================================================

    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    UPLOAD_FOLDER = os.getenv(
        "UPLOAD_FOLDER",
        str(BASE_DIR / "uploads")
    )

    # ======================================================
    # JWT Configuration
    # ======================================================

    SECRET_KEY = os.getenv("SECRET_KEY")

    ALGORITHM = os.getenv(
        "ALGORITHM",
        "HS256"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES",
            30
        )
    )

    # ======================================================
    # Database Configuration
    # ======================================================

    DB_HOST = os.getenv("DB_HOST")

    DB_PORT = int(
        os.getenv("DB_PORT", 3306)
    )

    DB_USER = os.getenv("DB_USER")

    DB_PASSWORD = os.getenv("DB_PASSWORD")

    DB_NAME = os.getenv("DB_NAME")

    # ======================================================
    # Gemini AI Configuration
    # ======================================================

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.5-flash"
    )


settings = Settings()