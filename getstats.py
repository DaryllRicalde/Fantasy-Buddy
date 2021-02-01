import flask
import json
import requests

def parameter():
    season = input("Which season?")
    #p_ID = input("Which player?")
    p_ID = 999999
    fname = input("Whats the first name?")
    lname = input("Whats the last name")
    url = "https://www.balldontlie.io/api/v1/players"
    response = requests.get(url)
    data = response.json()
    query = data["data"]
    while i < len(query):
        if fname in query and lname in query:
            p_ID = query["id"]
    param = "?seasons[]=" + season + "&player_ids[]=" + p_ID + "&postseason=false"
    #print (param)
    return param

def getStats():
    url = "https://www.balldontlie.io/api/v1/stats"
    param_url = url + parameter()
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
