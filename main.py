from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root(req: Request):
    return templates.TemplateResponse("home.html", {"request": req})


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.put("items/{item_id}")
def update_item(item_id: int, iem: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(req: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": req, "id": id})