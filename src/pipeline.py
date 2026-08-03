from src.pdf_engine import PDFEngine


def run_pipeline(pdf_path):

    engine = PDFEngine()

    pages = engine.page_count(pdf_path)

    print("=" * 50)
    print("AI PDF to DXF")
    print("=" * 50)
    print(f"Pages : {pages}")
