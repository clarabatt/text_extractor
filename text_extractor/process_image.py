import logging
from io import BytesIO

import pytesseract
from PIL import Image

logger = logging.getLogger(__name__)


def extract(content: bytes):
    try:
        image = Image.open(BytesIO(content))
        text = pytesseract.image_to_string(image)
        return text
    except Exception:
        logger.exception("OCR failed")
        raise
