# pip3 install "uvicorn[standard]" "fastapi[all]" mysql
# uvicorn --host 0.0.0.0 main:app --reload

import time
import sql

authPasswords = ["Catz@10kLakes"]

#database = mysql.connector.connect(host="10.30.222.109", user="meanscout", passwd="password", database="roboscout2")

#sqlcursor = database.cursor()

from typing import Optional

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import io
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://scouting.team4198.org",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

formdata = {
    "team": 4198,
    "match": 82,
    "absent": False,
    "teamlefttarm": True,
    "teamcollecte": False,
    "toppre": 2,
    "bottompre": 1,
    "missedpre": 0,
    "top": 3,
    "bottom": 2,
    "missed": 1,
    "safeareausag": "A Little",
    "defenceplaye": "A Little",
    "barnumberrea": 4,
    "teamattempts": True,
    "anyrobotprob": "No Problems",
    "extranotes": "This is an extra note.",
    "driveteamrat": "swaggy :)",
    "password": "password"
}

@app.get("/")
def read_root():
    return {"Hello": "World", "You probably": "shouldn't be looking at this"}

@app.post("/scouting")
def yes(item: sql.FormData):
    if item.password in authPasswords:
        #sql.AddForm(sqlcursor, database, item)
        sql.AddFormYes(item)
        return "Added Form"
    else:
        return "Auth Failure: Not Allowed"


@app.delete("/scouting")
def no(password: str):
    if password in authPasswords:
        #sql.RemoveAllForms(sqlcursor, database)
        #sql.ResetCsv()
        return "Remote Reset Dissalowed, Rejecting."
    else:
        return "Not Allowed"

@app.get("/scouting")
def maybe():
    #sql.GetAllForm(sqlcursor, database)

    memfile = io.StringIO(open("collected_surveys.csv", "r").read())
    response = StreamingResponse(memfile, media_type="text/csv")
    response.headers["Content-Disposition"] = f"inline; filename=yes.csv"

    return response
