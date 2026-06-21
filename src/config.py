import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DATA_FOLDER = "data"
DB_FOLDER = "db"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200