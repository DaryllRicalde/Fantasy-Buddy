import flask
import json
import requests

def parameter():
    season = input("Which season?")
    season = str(season)
    p_ID = 9999
    fname = input("Whats the first name?")
    lname = input("Whats the last name?")
    fname.lower()
    lname.lower()
    url = "https://www.balldontlie.io/api/v1/players?search=" + lname + "&per_page=100"
    response = requests.get(url)
    data = response.json()
    query = data["data"]
    i = 0
    while i < len(query):
        player_info = query[i]["first_name"]
        if player_info.lower() == fname:
            print(query[i]["id"])
            p_ID = query[i]["id"]
        i+=1

    param = "?seasons[]=" + season + "&player_ids[]=" + str(p_ID) + "&postseason=false"
    #print (param)
    return param

def getStats():
    url = "https://www.balldontlie.io/api/v1/stats"
    param_url = url + str(parameter())
    #print(param_url)
    response = requests.get(param_url)
    p_list = []
    data = response.json()
    #print(data)
    i = 0
    query = data["data"]
    while i < len(query):
        sub_dict = query[i]
        pts = sub_dict["pts"]
        p_list.append(pts)
        i+=1
    #append to some list
    print(p_list)
getStats()
