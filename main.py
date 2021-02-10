import requests
import config
import json

from flask import Flask, render_template, request

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

@app.route("/results/<playerID>", methods=["GET","POST"])
def player():

    
    return render_template("player.html")

# def getLogs():
#     url = "https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsBySeason/2020/20000441/all"
#     api_key = config.api_key
#     headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
#     jsonData = requests.get(url, headers=headers).json()
#     points = jsonData[0]["Points"]
#     print(data)

# def getPlayer():
#     url = "https://api.sportsdata.io/v3/nba/scores/json/Players"
#     api_key = config.api_key
#     headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
#     jsonData = requests.get(url, headers=headers).json()
#     fname = input("What is the player's first name?")
#     lname = input("What is the player's last name?")

#     i = 0
#     while i < len(jsonData):
#         if jsonData[i]["FirstName"].lower() == fname.lower() and jsonData[i]["LastName"].lower() == lname.lower():
#             print(jsonData[i]["PlayerID"])
#         i+= 1

if __name__ == "__main__":
    app.run()