import requests

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    
    labels = [
        '5','10','15','20','25','30'
        '35','40','45','50'
    ]
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run()