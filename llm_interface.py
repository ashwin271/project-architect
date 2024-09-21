from abc import ABC, abstractmethod

class LLMInterface(ABC):
    @abstractmethod
    def generate_response(self, prompt: str, temperature: float = 0.2, max_tokens: int = 1500) -> str:
        """
        Generate a response from the language model based on the given prompt.

        :param prompt: The input prompt to send to the LLM.
        :param temperature: Sampling temperature.
        :param max_tokens: Maximum number of tokens to generate.
        :return: The generated response as a string.
        """
        pass