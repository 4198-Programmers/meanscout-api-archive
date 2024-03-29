import mysql.connector
import time
from pydantic import BaseModel

# database = mysql.connector.connect(host="localhost", user="root", passwd="supersecretpassword", database="roboscout")

# mycursor = database.cursor()

class FormData(BaseModel):
    team: int
    matchnum: str
    absent: bool
    name: str
    location: str
    teamlefttarm: bool
    teamcollecte: bool
    toppre: int
    bottompre: int
    missedpre: int
    top: int
    bottom: int
    missed: int
    safeareausag: str
    defenceplaye: str
    barnumberrea: str
    teamattempts: bool
    roughestimat: str
    anyrobotprob: str
    extranotes: str
    driveteamrat: str
    password: str

formdatayes = {
    "team": 4198,
    "matchnum": 82,
    "absent": False,
    "name": "joey",
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
    "roughestimat": "",
    "anyrobotprob": "No Problems",
    "extranotes": "This is an extra note.",
    "driveteamrat": "swaggy :)",
    "password": "password"
}

def AddFormYes(formdata):
    formdata.extranotes = formdata.extranotes.replace(',', "")
    formdata.driveteamrat = formdata.driveteamrat.replace(",", "")
    formdata.roughestimat = formdata.roughestimat.replace(" seconds", "")
    #csvstuff = open("collected_surveys.csv", "r").read()
    formdata.absent = str(formdata.absent).replace("True", "TRUE").replace("False", "FALSE")
    formdata.teamlefttarm = str(formdata.teamlefttarm).replace("True", "TRUE").replace("False", "FALSE")
    formdata.teamcollecte = str(formdata.teamcollecte).replace("True", "TRUE").replace("False", "FALSE")
    formdata.teamattempts = str(formdata.teamattempts).replace("True", "TRUE").replace("False", "FALSE")
    csvstuff = f'{formdata.team}, {formdata.matchnum}, {formdata.absent}, {formdata.name}, {formdata.location}, {formdata.teamlefttarm}, {formdata.teamcollecte}, {formdata.toppre}, {formdata.bottompre}, {formdata.missedpre}, {formdata.top}, {formdata.bottom}, {formdata.missed}, "{formdata.safeareausag}", "{formdata.defenceplaye}", {formdata.barnumberrea}, {formdata.teamattempts}, {formdata.roughestimat}, "{formdata.anyrobotprob}", "{formdata.extranotes}", "{formdata.driveteamrat}"'
    if "\n" in csvstuff:
        csvstuff.replace("\n", "")
    csvstuff += "\n"
    with open("collected_surveys.csv", "a") as f:
        f.write(csvstuff)
        f.close()

def ResetCsv():
    with open("collected_surveys.csv", "w") as f:
        f.write("")

def AddForm(cursor, database, formdata):
    print(formdata)
    sqlFormula = "INSERT INTO info VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sqlFormTuple = (int(formdata.team), formdata.match, int(formdata.absent), int(formdata.teamlefttarm), int(formdata.teamcollecte), int(formdata.toppre), int(formdata.bottompre), int(formdata.missedpre), int(formdata.top), int(formdata.bottom), int(formdata.missed), formdata.safeareausag, formdata.defenceplaye, formdata.barnumberrea, int(formdata.teamattempts), formdata.anyrobotprob, formdata.extranotes, formdata.driveteamrat)
    cursor.execute(sqlFormula, sqlFormTuple)
    database.commit()
    return

def RemoveAllForms(cursor, database):
    sqlFormula = "DELETE FROM info"
    cursor.execute(sqlFormula)
    database.commit()
    return

def GetAllForm(cursor, database):
    sqlFormula = "SELECT * FROM info"
    cursor.execute(sqlFormula)
    result = cursor.fetchall()
    start = "team, match, absent, offtarmac, collectedballs, autotop, autobottom, automissed, teletop, telebottom, telemissed, safearea, defence, barnumber, climbattempt, notes, driverating"
    with open("collected_surveys.csv", "w") as f:
        f.write("")
        f.write(start + "\n")
    f = open("collected_surveys.csv", "a")
    for row in result:
        thing = ""
        for column in row:
            thing += f"{column}, "
        f.write(thing + "\n")

# def checkIfUser(cursor, accountName, password):
#     sqlFormula = "SELECT * FROM accounts"
#     cursor.execute(sqlFormula)
#     result = cursor.fetchall()
#     for user in result:
#         if user == (accountName, password):
#             authenticated = True
#             break
#         else:
#             authenticated = False
#     if authenticated:
#         return True
#     else:
#         return False

#  FOR INSERTING NEW THINGS INTO DATABASE
# sqlFormula = "INSERT INTO accounts (name, password) VALUES (%s, %s)"
#
# account1 = ("ANOTHERPLACEHOLDER", "heheanotherpassword")
#
# mycursor.execute(sqlFormula, account1)
#database.commit()
