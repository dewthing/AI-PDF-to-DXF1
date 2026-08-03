"""
PDF Engine
โหลด PDF และแปลงเป็นรูปภาพ
"""

from pathlib import Path
import fitz  # PyMuPDF


class PDFEngine:

    def __init__(self):
        pass

    def open(self, pdf_path):
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(pdf_path)

        return fitz.open(pdf_path)

    def page_count(self, pdf_path):
        doc = self.open(pdf_path)
        return len(doc)
