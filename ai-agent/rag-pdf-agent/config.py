from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
PERSIST_DIR = "db"
MODEL_NAME = "gpt-3.5-turbo"