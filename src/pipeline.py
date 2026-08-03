from src.pdf_engine import PDFEngine
from src.preprocessing import ImagePreprocessor
from src.ocr_engine import OCREngine


def run_pipeline(pdf_path):

    print("="*60)
    print("AI PDF to DXF")
    print("="*60)

    pdf = PDFEngine()

    pre = ImagePreprocessor()

    ocr = OCREngine()

    pages = pdf.page_count(pdf_path)

    print("Pages :", pages)

    print("Preprocessing Ready")

    print("OCR Ready")
