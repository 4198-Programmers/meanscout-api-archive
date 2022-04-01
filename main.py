# pip3 install "uvicorn[standard]" "fastapi[all]"
# uvicorn --host 0.0.0.0 main:app --reload

import time
import sql
import mysql.connector

authPassword = "CHANGETHIS"

database = mysql.connector.connect(host="localhost", user="root", passwd="password", database="roboscout")

sqlcursor = database.cursor()

from typing import Optional

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import io
from pydantic import BaseModel

app = FastAPI()

formdata = {
    "team": "4198",
    "match": "2",
    "absent": False,
    "offtarmac": True,
    "collectedballs": True,
    "autotop": 1,
    "autobottom": 2,
    "automissed": 10,
    "teletop": 10,
    "telebottom": 10,
    "telemissed": 69,
    "safearea": "A Little",
    "defence": "A Lot",
    "barnumber": "4",
    "climbattempt": True,
    "notes": "asd;lifjasef",
    "driverating": "10/10"
}

@app.get("/")
def read_root():
    return {"Hello": "World", "You probably": "shouldn't be looking at this"}

@app.post("/scouting")
def yes(item: sql.FormData):
    sql.AddForm(sqlcursor, database, item)
    return "Added Form"

@app.delete("/scouting")
def no(password: str):
    if password == authPassword:
        sql.RemoveAllForms(sqlcursor, database)
        return "Removed All Forms"
    else:
        return "Not Allowed"

@app.get("/scouting")
def maybe():
    sql.GetAllForm(sqlcursor, database)

    memfile = io.StringIO(open("asdf.csv", "r").read())
    response = StreamingResponse(memfile, media_type="text/csv")
    response.headers["Content-Disposition"] = f"inline; filename=yes.csv"

    return response

