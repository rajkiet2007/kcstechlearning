import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# Allow either GEMINI_API_KEY or GOOGLE_API_KEY; prefer GEMINI_API_KEY if set
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or GOOGLE_API_KEY
# Default model (can be overridden by GEMINI_MODEL env var).
# Use a model that supports generateContent per the Gemini Developer API.
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")