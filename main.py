# uvicorn main:app --reload

import time
import sql
import mysql.connector

database = mysql.connector.connect(host="root", user="root", passwd="supersecretpassword", database="roboscout")

sqlcursor = database.cursor()

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "You probably": "shouldn't be looking at this"}

@app.post("/")
def yes(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

