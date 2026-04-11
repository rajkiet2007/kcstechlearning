
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


class Model:

    def get_model(self,name):
        if name == "gpt":
            return init_chat_model("gpt-3.5-turbo")
        elif name == "gemini":
            # Ensure a Google API key is present and available to the client
            api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API")
            if not api_key:
                raise EnvironmentError(
                    "Google API key not set. Please set GEMINI_API_KEY in your environment or .env file."
                )
            # Make sure the env var is available for the underlying library
            os.environ["GEMINI_API_KEY"] = api_key
            return ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)
        else:
            raise ValueError(f"Model {self.name} not supported.")