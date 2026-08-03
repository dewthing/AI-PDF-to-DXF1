from pathlib import Path

def run_pipeline(pdf_path):

    print("="*60)
    print("AI PDF to DXF Converter")
    print("="*60)

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():

        print("Input file not found")

        return

    print(f"Input : {pdf_path}")

    print("Pipeline Started")

    print("Finish")
