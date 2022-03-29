import mysql.connector
import time

database = mysql.connector.connect(host="root@10.30.100.250", user="root", passwd="supersecretpassword", database="roboscout")

mycursor = database.cursor()

def AddAuthUser(cursor, database, accountName, password):
    sqlFormula = f"INSERT INTO authusers (username, password) VALUES (%s, %s)"
    cursor.execute(sqlFormula, (accountName, password))
    database.commit()

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
