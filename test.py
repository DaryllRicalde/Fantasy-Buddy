import config
import requests

api_key = config.api_key

def getHighestPts():
    url = "https://fly.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2021"  # Endpoint for stats by all players in 2020 season
    headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}
    jsonData = requests.get(url, headers=headers).json()

    max_ppg = 0
    points = 0
    games = 0
    i = 0

    while i < len(jsonData):
        curr_points = jsonData[i]["Points"]
        curr_games = jsonData[i]["Games"]
        if(curr_games != 0):
            curr_ppg = round(curr_points/curr_games,2) 
            if(curr_ppg > max_ppg):
                points = curr_points
                games = curr_games
                max_ppg = curr_ppg
        i += 1

    
    #highest_pts = round(max_pts / 82, 2) # 82 games
    highest_pts = max_ppg
    print(points)
    print(games)
    print(highest_pts)

getHighestPts()