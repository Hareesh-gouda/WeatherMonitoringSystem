
import requests
from datetime import datetime


# Replace with your actual OpenWeatherMap API key
API_KEY = 'bd5e378503939ddaee76f12ad7a97608'  # Ensure this is a valid key
CITY_IDS = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_weather_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            'main': data['weather'][0]['main'],  # Main weather condition (e.g., Rain, Clear)
            'temp': data['main']['temp'],  # Temperature in Celsius
            'feels_like': data['main']['feels_like'],  # Feels like temperature in Celsius
            'dt': datetime.fromtimestamp(data['dt']),  # Time of the data update
        }
    else:
        print(f"Error fetching data for {city}: {response.status_code} - {response.text}")
        return None

def get_weather_for_all_cities():
    """Fetches weather data for all predefined cities."""
    weather_data = {}
    for city in CITY_IDS:
        data = get_weather_data(city)
        if data:
            weather_data[city] = data
    return weather_data

if __name__ == '__main__':
    # Example usage: fetch and print weather data for all cities
    all_weather_data = get_weather_for_all_cities()
    for city, data in all_weather_data.items():
        print(f"Weather in {city}:")
        print(f"  Main: {data['main']}")
        print(f"  Temperature: {data['temp']}°C")
        print(f"  Feels Like: {data['feels_like']}°C")
        print(f"  Updated at: {data['dt']}\n")
