# alert.py
def check_alerts(weather_data, thresholds):
    for data in weather_data:
        if data['temp'] > thresholds['temp']:
            print(f"Alert: High temperature in {data['city']} - {data['temp']}°C")