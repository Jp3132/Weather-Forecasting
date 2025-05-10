from flask import Flask,render_template
import os

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    visuals_path = ["cloud cover.png",
                    "humidity.png",
                    "pressue.png",
                    "rain.png",
                    "snow.png",
                    "temperature.png",
                    "wind_speed.png"]
    return render_template('home.html',images = visuals_path)

@app.route("/forecast")
def forecast():
    return render_template('forecast.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)