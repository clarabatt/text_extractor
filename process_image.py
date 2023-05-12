from io import BytesIO
from PIL import Image
import pytesseract


def extract(content: bytes):
    image = Image.open(BytesIO(content))
    text = pytesseract.image_to_string(image)
    return text
