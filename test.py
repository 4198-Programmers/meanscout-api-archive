import requests
import sql
import json

formdata = {
    "team": "4198",
    "match": "3",
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

yes = requests.delete("http://127.0.0.1:8000/scouting")

print(yes)
print(yes.text)

# import time
#
# print("yes", end="\r")
# time.sleep(2)
# print("                                ", end="\r")
# print("no\r")