# visualizations.py
import matplotlib.pyplot as plt
from models.models import WeatherSummary

def plot_weather_summary():
    summaries = WeatherSummary.query.all()
    dates = [summary.date for summary in summaries]
    avg_temps = [summary.average_temp for summary in summaries]

    plt.plot(dates, avg_temps)
    plt.title('Average Daily Temperatures')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.show()