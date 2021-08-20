import requests
import config
import json
import datetime

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

api_key = config.api_key # API Key
now = datetime.datetime.now()
this_year = now.year #Current year
global_header = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}

@app.route("/")
def index():
    url = "https://api.sportsdata.io/v3/nba/scores/json/Players" 
    headers = global_header
    jsonData = requests.get(url, headers=headers).json()

    return render_template("home.html")

@app.route("/search") # Page where users will search for the player
def search():

    return render_template("search.html")

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error_500.html'),500

@app.route("/test")
def test():

    playerID,playerImage,team,position = getPlayer("Bradley","Beal")
    ppg= getLogs(playerID)

    data = [
        ("PPG", ppg),
        ("APG", 9)
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("test.html", labels=labels, values=values,team=team,position=position,ppg=ppg)

@app.route("/player",methods=["GET","POST"])
def player():

    firstName = request.form["firstName"] # Player's first name
    lastName = request.form["lastName"] # Player's last name

    playerID,playerImage,team,position = getPlayer(firstName,lastName)
    ppg,apg,rpg,tpg= getLogs(playerID) # Get stats

    highest_ppg = getHighestPts()

    points_data = [
        ("This player's PPG", ppg),
        ("2020 Regular Season PPG Leader", highest_ppg)
    ]

    pts_labels = [row[0] for row in points_data]
    pts_values = [row[1] for row in points_data]

    ast_data = [
        ("This player's APG", apg),
        ("2020 Regular Season APG Leader", 10.2)
    ]

    ast_labels = [row[0] for row in ast_data]
    ast_values = [row[1] for row in ast_data]

    reb_data = [
        ("This player's RPG", rpg),
        ("2020 Regular Season RPG Leader", 15.2)
    ]

    reb_labels = [row[0] for row in reb_data]
    reb_values = [row[1] for row in reb_data]

    to_data = [
        ("This player's TOPG", tpg),
        ("2020 Regular Season TOPG Leader", 5)
    ]

    to_labels = [row[0] for row in to_data]
    to_values = [row[1] for row in to_data]

    
    return render_template("player.html",
    firstName=firstName,
    lastName = lastName,
    team=team,
    image = playerImage,
    position = position,
    ppg = ppg,
    pts_labels = pts_labels,
    pts_values = pts_values,
    ast_labels = ast_labels,
    ast_values = ast_values,
    reb_labels = reb_labels,
    reb_values = reb_values,
    to_labels = to_labels,
    to_values = to_values
    )

def getHighestPts():
    url = "https://fly.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/" + str(this_year) # Endpoint for stats by all players in 2020 season
    headers = global_header
    jsonData = requests.get(url, headers=headers).json()

    max_pts = 0
    i = 0
    highest_pts = 0

    while i < len(jsonData):
        points = jsonData[i]["Points"]
        if(points > max_pts):
            max_pts = points
        i += 1

    
    highest_pts = round(max_pts / 82, 2) # 82 games
    return highest_pts 


def getHighestAst():
    url = "https://fly.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/" + str(this_year) # Endpoint for stats by all players in 2020 season
    headers = global_header
    jsonData = requests.get(url, headers=headers).json()   
    i = 0

def getHighestReb():
    url = "https://fly.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/" + str(this_year) # Endpoint for stats by all players in 2020 season
    headers = global_header
    jsonData = requests.get(url, headers=headers).json()    
    i = 0

def getHighestTO():
    url = "https://fly.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/" + str(this_year) # Endpoint for stats by all players in 2020 season
    headers = global_header
    jsonData = requests.get(url, headers=headers).json()    

    i = 0

def getLogs(playerID): #Gets points and other stats averaged

    url = "https://fly.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/" + str(this_year) # Endpoint for stats by all players in 2020 season
    headers = global_header
    jsonData = requests.get(url, headers=headers).json()

    ppg = 0
    i = 0
    while i < len(jsonData):
        if jsonData[i]["PlayerID"] == playerID:
            points = jsonData[i]["Points"]
            assists = jsonData[i]["Assists"]
            rebs = jsonData[i]["Rebounds"]
            turnovrs = jsonData[i]["Turnovers"]
            games = jsonData[i]["Games"]
            ppg = round(points / games, 2) # round up to two decimal places
            apg = round(assists / games, 2)
            rpg = round(rebs / games, 2)
            tpg = round(turnovrs / games, 2)
        i += 1

    return ppg,apg,rpg,tpg


def getPlayer(firstName,lastName): # Gets a player 
    url = "https://api.sportsdata.io/v3/nba/scores/json/Players"
    headers = global_header
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