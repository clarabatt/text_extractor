from fastapi import FastAPI, Request, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from text_extractor import process_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(req: Request):
    return templates.TemplateResponse("home.html", {"request": req})


@app.post("/upload")
async def upload_file(req: Request, file: UploadFile | None = None):
    if not file:
        return templates.TemplateResponse(
            "home.html", {"request": req, "text": "No file uploaded"}
        )

    content = await file.read()
    filename = file.filename
    text = process_image.extract(content)
    return templates.TemplateResponse(
        "home.html", {"request": req, "text": text, "filename": filename}
    )
