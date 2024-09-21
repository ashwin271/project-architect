import openai
import os
from dotenv import load_dotenv
from llm_interface import LLMInterface

# Load environment variables from .env file
load_dotenv()

class OpenAIModel(LLMInterface):
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set in environment variables or .env file.")
        openai.api_key = self.api_key

    def generate_response(self, prompt: str, temperature: float = 0.2, max_tokens: int = 1500) -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You help convert detailed architecture descriptions into file structures with boilerplate content."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message['content']
        except Exception as e:
            raise RuntimeError(f"OpenAI API request failed: {e}")
