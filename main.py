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

@app.route("/search") # Page where users will search for the player
def search():

    return render_template("search.html")

@app.route("/player",methods=["GET","POST"])
def player():

    firstName = request.form["firstName"] # Player's first name
    lastName = request.form["lastName"] # Player's last name

    playerID,playerImage,team,position = getPlayer(firstName,lastName)
    p_points = getLogs(playerID)

    
    return render_template("player.html",
    firstName=firstName,
    lastName = lastName,
    team=team,
    image = playerImage,
    position = position,
    points=p_points
    )

def getLogs(playerID): #Gets points and other stats
    url = "https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsBySeason/2020/" + str(playerID) + "/all" # Add player ID to URL to get this player's stats
    api_key = config.api_key
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()
    points_list = [] 

    for i in range(len(jsonData)):
        points = jsonData[i]["Points"]
        points_list.append(points)
        i += 1

    return points_list

def getPlayer(firstName,lastName): # Gets a player 
    url = "https://api.sportsdata.io/v3/nba/scores/json/Players"
    api_key = config.api_key
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()

    playerID = 99999

    i = 0
    while i < len(jsonData):
        if jsonData[i]["FirstName"].lower() == firstName.lower() and jsonData[i]["LastName"].lower() == lastName.lower(): #if we find the player that match the query
            playerID = jsonData[i]["PlayerID"]
            playerImg = jsonData[i]["PhotoUrl"]
            team = jsonData[i]["Team"]
            position = jsonData[i]["Position"]
        i+= 1

    return playerID,playerImg,team,position


if __name__ == "__main__":
    app.run()