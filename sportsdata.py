from requests.auth import HTTPBasicAuth
import flask
import json
import requests
import config

def getLogs():
    url = "https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsBySeason/2020/20000441/all"
    api_key = config.api_key
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()
    points = jsonData[0]["Points"]
    print(data)

def getPlayer():
    url = "https://api.sportsdata.io/v3/nba/scores/json/Players"
    api_key = config.api_key
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()
    fname = input("What is the player's first name?")
    lname = input("What is the player's last name?")

    i = 0
    while i < len(jsonData):
        if jsonData[i]["FirstName"].lower() == fname.lower() and jsonData[i]["LastName"].lower() == lname.lower():
            print(jsonData[i]["PlayerID"])
        i+= 1
getPlayer()