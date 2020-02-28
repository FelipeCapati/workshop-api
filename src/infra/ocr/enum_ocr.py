from enum import Enum
from src.infra.ocr.tesseract_ocr import TesseractOCR
from src.infra.ocr.azure_ocr import AzureOCR


class OcrType(Enum):
    TesseractOCR = TesseractOCR()
    AzureOCR = AzureOCR
