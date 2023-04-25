# Text Extractor

Extracts text from pdfs and images using [tesseract](https://pypi.org/project/pytesseract/).


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
uvicorn main:app --reload
```
