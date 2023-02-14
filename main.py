from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float


app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int,):
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict