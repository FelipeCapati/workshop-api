from abc import ABC, abstractmethod


class AbstractOCR(ABC):
    @staticmethod
    @abstractmethod
    def image_to_text(path_file: str, delete: bool = False) -> str:
        pass
