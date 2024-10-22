# test_app.py
import unittest
from app import app, db
# test_app.py
#import unittest
from services.weather import get_weather_data  # Adjust the import according to your project structure
from services.aggregator import aggregate_weather_data

class WeatherAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_weather_data_retrieval(self):
        # Simulate a weather data retrieval
        response = get_weather_data('Delhi')
        self.assertIsNotNone(response)

    def test_daily_summary_calculation(self):
        # Simulate daily summary calculations
        weather_data = [
            {'temp': 30, 'main': 'Clear'},
            {'temp': 32, 'main': 'Clear'},
            {'temp': 28, 'main': 'Clear'},
        ]
        summary = aggregate_weather_data(weather_data)
        self.assertAlmostEqual(summary.average_temp, 30)

# Run tests
if __name__ == '__main__':
    unittest.main()