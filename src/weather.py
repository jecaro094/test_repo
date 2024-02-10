import pyowm
import requests

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = "96b231ebb0d488f2a21da1c8e0026d9b"

owm = pyowm.OWM(api_key)
mgr = owm.weather_manager()
# Example: Getting weather information by city name
# city_name = 'London'
# observation = owm.weather_at_place(city_name)
# w = observation.get_weather()


def get_weather(city_name):
    # one_call = mgr.one_call(lat=52.5244, lon=13.4105)
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()


# print(f"Weather in {city_name}:")
# print(f"Temperature: {w.get_temperature('celsius')['temp']}°C")
# print(f"Status: {w.get_status()}")
# print(f"Wind speed: {w.get_wind()['speed']} m/s")
# print(f"Humidity: {w.get_humidity()}%")
