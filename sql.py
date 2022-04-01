import mysql.connector
import time
from pydantic import BaseModel

# database = mysql.connector.connect(host="localhost", user="root", passwd="supersecretpassword", database="roboscout")

# mycursor = database.cursor()

class FormData(BaseModel):
    team: str
    match: str
    absent: bool
    offtarmac: bool
    collectedballs: bool
    autotop: int
    autobottom: int
    automissed: int
    teletop: int
    telebottom: int
    telemissed: int
    safearea: str
    defence: str
    barnumber: str
    climbattempt: bool
    notes: str
    driverating: str

def AddForm(cursor, database, formdata):
    print(formdata)
    sqlFormula = "INSERT INTO info VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sqlFormTuple = (formdata.team, formdata.match, int(formdata.absent), int(formdata.offtarmac), int(formdata.collectedballs), int(formdata.autotop), int(formdata.autobottom), int(formdata.automissed), int(formdata.teletop), int(formdata.telebottom), int(formdata.telemissed), formdata.safearea, formdata.defence, formdata.barnumber, int(formdata.climbattempt), formdata.notes, formdata.driverating)
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
    with open("asdf.csv", "w") as f:
        f.write("")
        f.write(start + "\n")
    f = open("asdf.csv", "a")
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
