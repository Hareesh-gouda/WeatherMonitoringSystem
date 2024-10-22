# models/models.py
from flask_sqlalchemy import SQLAlchemy

 #Initialize the SQLAlchemy instance
db = SQLAlchemy()

class WeatherSummary(db.Model):
    __tablename__ = 'weather_summaries'  # Optional: Specify a custom table name

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    average_temp = db.Column(db.Float, nullable=False)
    max_temp = db.Column(db.Float, nullable=False)
    min_temp = db.Column(db.Float, nullable=False)
    dominant_condition = db.Column(db.String(50), nullable=False)  # Specify max length for better DB design

    def __repr__(self):
        return f'<WeatherSummary date={self.date}, avg_temp={self.average_temp}>'
