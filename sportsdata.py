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
    print(jsonData)

getLogs()