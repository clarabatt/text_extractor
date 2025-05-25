# Text Extractor

Extracts text from pdfs and images using [tesseract](https://pypi.org/project/pytesseract/).

<img src="static/img/example.png" alt="My Image" width="500"/>

**Technologies**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

## How to run

Installing dependencies:

```shell
uv sync
```

Running the project:

```shell
# Activate the virtual environment
source .venv/bin/activate

# Running the project
uv run uvicorn text_extractor.main:app --reload
```
