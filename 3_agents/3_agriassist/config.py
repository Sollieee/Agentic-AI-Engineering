import os
from pathlib import Path
from dotenv import load_dotenv

# Locate the AgriAssist project directory
PROJECT_ROOT = Path(__file__).resolve().parent

# Load the existing .env file from the main repository
load_dotenv(PROJECT_ROOT.parent.parent / ".env")

# Read the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY was not found. Check the root .env file."
    )

OPENAI_MODEL = "gpt-5.4-mini"
