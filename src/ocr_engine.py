"""
OCR Engine
"""

import easyocr


class OCREngine:

    def __init__(self):

        self.reader = easyocr.Reader(
            ['en', 'th'],
            gpu=False
        )

    def detect(self, image):

        result = self.reader.readtext(image)

        return result
