from src.infra.ocr.abstract_ocr import AbstractOCR


class TesseractOCR(AbstractOCR):
    def __init__(self):
        pass

    @staticmethod
    def image_to_text(path_file: str, delete: bool = False) -> str:
        return "TESSERACT IMPLEMENTATION"
