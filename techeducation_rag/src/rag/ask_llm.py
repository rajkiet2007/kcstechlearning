from openai import OpenAI
import os
from dotenv import load_dotenv
import google.generativeai as genai

class AskLLM:
    def __init__(self, name: str, provider: str):
        self.name = name
        self.provider = provider

    def get_model_name(self):
        if self.name == "openai":
            return "gpt-4"
        elif self.name == "gemini":
            return "gemini-3-flash-preview"

        else:
            raise ValueError("Unsupported model name. Please choose 'gpt' or 'gemini'.")
        
    def get_client(self):
        if self.provider == "openai":
            return OpenAI(
                api_key=os.getenv("OPENAI_API_KEY")
            )
        
        elif self.provider == "gemini":
            return OpenAI(
                api_key=os.getenv("GEMINI_API_KEY"),
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
            )
        
        else:
            raise ValueError("Unsupported provider")