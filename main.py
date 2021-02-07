import requests
import config

from flask import Flask, render_template, request

app = Flask(__name__)

key = config.api_key

@app.route("/")
def index():
    
    return render_template("home.html")

@app.route("/search")
def search():

    return render_template("search.html")

if __name__ == "__main__":
    app.run()