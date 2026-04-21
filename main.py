from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items: List[Item] = []

@app.get('/')
def root():
    return {'Hello': 'World'}

@app.get('/items', response_model=List[Item])
def list_item(limit:int = 10) -> List[Item]:
    return items[:limit]

@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(
            status_code= 404,
            detail='The requested item cannot be found.'
        )
    
@app.post('/items', response_model=Item)
def create_item(item: Item) -> Item:
    items.append(item)
    print(items)
    return item
