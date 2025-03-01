from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()  # this is to get our api key from .env file

def get_current_weather(city='Tirupati'):

    request_url= f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data=requests.get(request_url).json()

    return weather_data     # this will get data from the weathermap website through the given api key.

# python code to enter the city name and to to get the weather data.

if __name__ == "__main__":
    print('\n**** Get Current Weather Conditions ****\n')

    city=input("enter a city name: ")

    # checking if city name is given empty or full of whitespaces.
    if not bool(city.strip()):
        city="Bengaluru"

    weather_data= get_current_weather(city)

    print('\n')
    pprint(weather_data)
          