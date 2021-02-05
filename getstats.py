import flask
import json
import requests

def parameter():
    season = input("Which season?\n")
    #p_ID = input("Which player?")
    p_ID = 999999
    fname = input("Whats the first name?\n")
    lname = input("Whats the last name?\n")
    fname = fname.lower()
    lname = lname.lower()
    url = "https://www.balldontlie.io/api/v1/players?search=" + lname + "&per_page=100"
    response = requests.get(url)
    data = response.json()
    query = data["data"]
    i = 0
    while i < len(query):        
        sub_dict = query[i]
        if fname == str(sub_dict["first_name"]).lower():            
            p_ID = sub_dict["id"]
            print(p_ID)
                   
        i+=1
    param = "?seasons[]=" + str(season) + "&player_ids[]=" + str(p_ID) + "&postseason=false"
    #print(p_ID)
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
