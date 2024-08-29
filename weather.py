import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass


# loading the environment variables
load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class weatherData:
    main: str
    description: str
    icon: str
    temperature: str



# creating a function called get_lat_long - queries the specific endpoint of the API to return the latitude and longitude of a location
def get_lat_long(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    # access the lat and long from the dictionary within the list
    lat, long = resp[0].get('lat'), resp[0].get('lon')
    return lat, long


def get_current_weather(lat, long, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_key}&units=metric').json() # kelvin to celsius 
    print(resp)
    


# # testing if this API call helps grab information about a particular state
# get_lat_long('London', 'Kentucky', 'US', api_key)

if __name__ == '__main__':
    lat, long = get_lat_long('Toronto', 'ON', 'Canada', api_key)
    get_current_weather(lat, long, api_key) # passing the latitude and the longitude to the function to get information about the weather