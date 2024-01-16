from fastapi import FastAPI
from typing import Union
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ya responde el servidor
app = FastAPI()

# ruta por defecto
@app.get("/")
def prueba():
  return "Prueba"

# ruta get
@app.get("/items/{items_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}

# ruta post
""" @app.post("/items"y)
def create_item()

@app.put("/items/")
    def put_items()
    
@app.delete("/items/{items_id}")
    delete_items()
    
@app. """
