<<<<<<< HEAD:requests.py
=======
import flask
import json
>>>>>>> 16ce8c63926f77124469f740a981738305ef3128:getstats.py
import requests

def parameter():
    season = input("Which season?")
    p_ID = input("Which player?")
    param = "?seasons[]=" + season + "&player_ids[]=" + p_ID + "&postseason=false"
    print (param)
    return param

def getStats():
    url = "https://www.balldontlie.io/api/v1/stats"
    param_url = url + parameter()
    print(param_url)
    response = requests.get(param_url)

    data = response.json()
    print(data)
    i = 0
    while True:
        query = data["data"][i]
        pts = query["pts"]
        print(pts)
        i+=1

getStats()
