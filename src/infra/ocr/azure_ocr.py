from src.infra.ocr.abstract_ocr import AbstractOCR


class AzureOCR(AbstractOCR):
    def __init__(self):
        pass

    @staticmethod
    def image_to_text(path_file: str, delete: bool = False) -> str:
        return "AZURE IMPLEMENTATION"
