# aggregator.py
from models.models import WeatherSummary
from datetime import date

def aggregate_weather_data(weather_data):
    today = date.today()
    daily_summary = WeatherSummary(
        date=today,
        average_temp=sum(d['temp'] for d in weather_data) / len(weather_data),
        max_temp=max(d['temp'] for d in weather_data),
        min_temp=min(d['temp'] for d in weather_data),
        dominant_condition=get_dominant_condition(weather_data)
    )
    return daily_summary

def get_dominant_condition(weather_data):
    conditions = [d['main'] for d in weather_data]
    return max(set(conditions), key=conditions.count)