# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from weather import get_weather_data
from aggregator import aggregate_weather_data
from weather import CITY_IDS
from models.models import db


scheduler = BackgroundScheduler()

def scheduled_job():
    weather_data = []
    for city in CITY_IDS:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)

    if weather_data:
        summary = aggregate_weather_data(weather_data)
        # Save summary to the database
        db.session.add(summary)
        db.session.commit()

scheduler.add_job(scheduled_job, 'interval', minutes=5)
scheduler.start()