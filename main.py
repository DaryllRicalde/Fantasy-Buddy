import requests
import config
import json

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

key = config.api_key

@app.route("/")
def index():

    url = "https://api.sportsdata.io/v3/nba/scores/json/Players"
    api_key = config.api_key
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()

    return render_template("home.html")

@app.route("/search")
def search():

    return render_template("search.html")

@app.route("/player",methods=["GET","POST"])
def player():

    firstName = request.form["firstName"]
    lastName = request.form["lastName"]

    playerID, playerImage = getPlayer(firstName,lastName)
    p_points = getLogs(playerID)


    
    return render_template("player.html",
    firstName=firstName,
    playerID=playerID,
    image = playerImage,
    points=p_points
    )

def getLogs(playerID):
    url = "https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsBySeason/2020/" + str(playerID) + "/all"
    api_key = config.api_key
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()
    points_list = []

    for i in range(len(jsonData)):
        points = jsonData[i]["Points"]
        points_list.append(points)
        i += 1

    return points_list

def getPlayer(firstName,lastName):
    url = "https://api.sportsdata.io/v3/nba/scores/json/Players"
    api_key = config.api_key
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()

    playerID = 99999
    playerImg = ""

    i = 0
    while i < len(jsonData):
        if jsonData[i]["FirstName"].lower() == firstName.lower() and jsonData[i]["LastName"].lower() == lastName.lower():
            playerID = jsonData[i]["PlayerID"]
            playerImg = jsonData[i]["PhotoUrl"]
        i+= 1



    return playerID,playerImg
if __name__ == "__main__":
    app.run()