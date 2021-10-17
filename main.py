
from flask import Flask, app, render_template, request, redirect, url_for, make_response
import requests
import os

try:
    import secrets
except ImportError as e:
    pass

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    query = "Podnanos,SLO"
    unit = "metric"
    api_key = os.environ.get("API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)
    data = requests.get(url=url) #GET request to OpenWeatherMap api
    return render_template("index.html", data=data.json())


if __name__=="__main__":
    app.run()