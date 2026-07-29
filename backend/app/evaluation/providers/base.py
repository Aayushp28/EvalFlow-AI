from abc import ABC, abstractmethod


class BaseProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str):
        """
        Generate a response from the model.
        """
        pass