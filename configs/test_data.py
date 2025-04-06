from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

VALID_USER = {
    "name": os.getenv("USER_NAME"),
    "surname": os.getenv("USER_SURNAME"),
    "email": os.getenv("USER_EMAIL"),
    "telephon": os.getenv("USER_PHONE"),
    "message": os.getenv("USER_MESSAGE"),
}

INVALID_USER = {
    "name": "",
    "surname": os.getenv("USER_SURNAME"),
    "email": "",
    "telephon": os.getenv("USER_PHONE"),
    "message": os.getenv("USER_MESSAGE"),
}
