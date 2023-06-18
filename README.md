# Text Extractor

Extracts text from pdfs and images using [tesseract](https://pypi.org/project/pytesseract/).

**Technologies**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)


## How to run

This project uses Poetry as dependency manager. [To install Poetry follow their documentation.](https://python-poetry.org/docs/)

Installing dependencies:

```shell
poetry install
```

Running the project:


```shell
# Activate the virtual environment
poetry shell

# Running the project
uvicorn text_extractor.main:app --reload
```
