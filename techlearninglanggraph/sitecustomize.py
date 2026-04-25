from dotenv import load_dotenv
import os

# Load .env automatically for any Python process started in this project
load_dotenv()

# Optional: expose a debug print when running locally
if os.getenv("LANGSMITH_API_KEY"):
    print("sitecustomize: LANGSMITH_API_KEY loaded")
else:
    print("sitecustomize: LANGSMITH_API_KEY not found")
