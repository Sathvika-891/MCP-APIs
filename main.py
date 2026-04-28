from fastapi import FastAPI
from pydantic import BaseModel
import logging
logger = logging.getLogger("api")
class Item(BaseModel):
    id:int
    name: str
    value: int
app = FastAPI()
items={}
@app.get("/")
def read_root():    return {"Hello": "World"}
@app.post("/data")
def create_data(item: Item):
    # items.update({item.name: item.value})
    logger.info(f"Received item: {item}")
    if item.id not in items:
        items[item.id] = {"name": item.name, "value": item.value}
        
    return {"Received": item}

@app.get("/items")
def get_items():
    return {"items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if len(items) == 0:
        return {"message": "No items found"}
    logger.info(f"Retrieving item with id: {item_id}")
    return {"item_id": items.get(item_id, "Item not found")}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        logger.info(f"Deleting item with id: {item_id}")
        del items[item_id]
        return {"message": f"Item with id {item_id} deleted"}
    else:
        return {"message": "Item not found"}
    
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)