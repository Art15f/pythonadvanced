from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"meassage":"Hello, world!"}

@app.get("/items")
def read_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Dion Kabashi"}

@app.get("/items")
def get_items(skip: int=0, limit: int=10):
    return {"skip":skip, "limit":limit}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "item_name": name, "item_price":price}


@app.post("/items/")
def create_item(name: str, price: float):
    return {"item_name": name, "item_price": price}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message":f"Item {item_id} deleted"}

























































