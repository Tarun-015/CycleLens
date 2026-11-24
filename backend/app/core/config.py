
import os
from pathlib import Path

from dotenv import load_dotenv

# Locate the backend directory
BACKEND_DIR = Path(__file__).resolve().parents[2]

# Load environment variables from backend/.env
load_dotenv(BACKEND_DIR / ".env")

# Use SQLite by default
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{(BACKEND_DIR / 'cyclelens.db').as_posix()}"
)
