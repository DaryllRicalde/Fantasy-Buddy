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

<<<<<<< HEAD
@app.route("/player",methods=["GET","POST"])
def player():

    firstName = request.form["firstName"]
    lastName = request.form["lastName"]

    playerID = getPlayer(firstName,lastName)


    
    return render_template("player.html",
    firstName=firstName,
    playerID=playerID
    )
=======
@app.route("/results/<playerID>", methods=["GET","POST"])
def player():

    
    return render_template("player.html")
>>>>>>> master

# def getLogs():
#     url = "https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsBySeason/2020/20000441/all"
#     api_key = config.api_key
#     headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
#     jsonData = requests.get(url, headers=headers).json()
#     points = jsonData[0]["Points"]
#     print(data)

def getPlayer(firstName,lastName):
    url = "https://api.sportsdata.io/v3/nba/scores/json/Players"
    api_key = config.api_key
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()

    i = 0
    while i < len(jsonData):
        if jsonData[i]["FirstName"].lower() == firstName.lower() and jsonData[i]["LastName"].lower() == lastName.lower():
            playerID = jsonData[i]["PlayerID"]
        i+= 1

    return playerID
if __name__ == "__main__":
    app.run()