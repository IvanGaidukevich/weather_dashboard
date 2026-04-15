import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
API_DAYS = os.getenv("API_DAYS")
API_LANG = os.getenv("API_LANG")


def load_data(city: str) -> dict:
    response = requests.get(API_URL, params={
        "key": API_KEY,
        "q": city,
        "days": API_DAYS,
        "lang": API_LANG
    })
    data = response.json()

    city_name = data["location"]["name"]
    condition = data["current"]["condition"]["text"]
    icon = data["current"]["condition"]["icon"]
    temp = data["current"]["temp_c"]
    forecast_hours = data["forecast"]["forecastday"][0]["hour"]
    temps = [hour["temp_c"] for hour in forecast_hours]
    ap = [hour["pressure_mb"] * 0.75 for hour in forecast_hours]
    wind = [hour["wind_kph"] * 0.28 for hour in forecast_hours]
    wind_dirs = [hour["wind_degree"] for hour in forecast_hours]
    hours = [hour["time"][-5:] for hour in forecast_hours]

    return {
        "city": city_name,
        "condition": condition,
        "icon": icon,
        "temp": temp,
        "temps": temps,
        "ap": ap,
        "wind": wind,
        "wind_dirs": wind_dirs,
        "hours": hours
    }