"""
Image Preprocessing
"""

import cv2
import numpy as np


class ImagePreprocessor:

    def __init__(self):
        pass

    def to_gray(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def blur(self, image):
        return cv2.GaussianBlur(image, (5, 5), 0)

    def threshold(self, image):
        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            15,
            2,
        )

    def preprocess(self, image):

        gray = self.to_gray(image)

        blur = self.blur(gray)

        binary = self.threshold(blur)

        return binary
