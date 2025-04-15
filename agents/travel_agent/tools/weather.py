# weather.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather_forecast(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Process data: summarize weather for next 3–5 days
    forecast_summary = {}

    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        weather = item["weather"][0]["main"]
        temp = item["main"]["temp"]

        if date not in forecast_summary:
            forecast_summary[date] = {
                "weather": weather,
                "temp": [temp]
            }
        else:
            forecast_summary[date]["temp"].append(temp)

    # Simplify to daily average
    for date in forecast_summary:
        temps = forecast_summary[date]["temp"]
        forecast_summary[date]["avg_temp"] = sum(temps) / len(temps)
        del forecast_summary[date]["temp"]

    return forecast_summary

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    forecast = get_weather_forecast(city_name)
    print(forecast)
