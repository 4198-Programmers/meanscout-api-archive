import requests
import sql
import json

formdatayes = {
    "team": 4198,
    "match": "82",
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
    "barnumberrea": "4",
    "teamattempts": True,
    "anyrobotprob": "No Problems",
    "extranotes": "This is an extra note.",
    "driveteamrat": "swaggy :)",
    "password": "password"
}

yes = requests.post("https://data.team4198.org:8000/scouting", json=formdatayes)

print(yes)
print(yes.text)

# import time
#
# print("yes", end="\r")
# time.sleep(2)
# print("                                ", end="\r")
# print("no\r")