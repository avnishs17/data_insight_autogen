from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv

from config.constants import MODEL_GEMINI

def get_llm_client():
    
    load_dotenv()
    gemini_model_client = OpenAIChatCompletionClient(
        model=MODEL_GEMINI,
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    return gemini_model_client