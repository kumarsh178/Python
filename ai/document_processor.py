import os
import fitz
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


def extract_text_from_image(image_path):

    img = Image.open(image_path)

    text = pytesseract.image_to_string(img)
    return text


def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    # If PDF already contains text
    if text.strip():
        return text

    # Otherwise run OCR
    images = convert_from_path(pdf_path)

    for img in images:
        text += pytesseract.image_to_string(img)
    return text


def process_document(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)

    elif ext == ".pdf":
        return extract_text_from_pdf(file_path)

    return ""