from src.pdf_engine import PDFEngine
from src.preprocessing import ImagePreprocessor


def run_pipeline(pdf_path):

    print("="*60)
    print("AI PDF to DXF")
    print("="*60)

    pdf = PDFEngine()

    pre = ImagePreprocessor()

    pages = pdf.page_count(pdf_path)

    print("Pages :", pages)

    print("Preprocessing Ready")
