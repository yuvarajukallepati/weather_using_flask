from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve                      # this is to change our development server into production server.

app=Flask(__name__)     # this makes our app as the flaskapp.

@app.route('/')     # this used to route in our web application
@app.route('/index')  # these are similar to urls.py in django.

def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city=request.args.get('city')

    # checking if city name is given empty or full of whitespaces.
    if not bool(city.strip()):
        city="Tirupati"

    weather_data = get_current_weather(city)

    # city is not found by api key
    if not weather_data['cod'] == 200:
        return render_template('citynotfound.html')
    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
    )

if __name__ == "__main__":
    # app.run(host="0.0.0.0",port=8000)       # this is to run our program in our localhost/pc.
    serve(app, host="0.0.0.0",port=8000)        # this is for production server.