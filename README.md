# Weather Monitoring System

## Overview
The Weather Monitoring System is a real-time data processing application that retrieves and analyzes weather data from the OpenWeatherMap API. It provides summarized insights, alerts for extreme weather conditions, and visualizations of weather trends.

## Features
- **Real-Time Data Retrieval**: Continuously fetches weather data for major cities in India every 5 minutes.
- **Data Aggregation**: Computes daily weather summaries including average, maximum, and minimum temperatures, and identifies dominant weather conditions.
- **Alerts**: Triggers alerts based on user-configured thresholds for temperature and weather conditions.
- **Visualizations**: Displays daily weather summaries and trends using Matplotlib.

## Technologies Used
- Flask
- SQLAlchemy
- APScheduler
- Matplotlib
- Requests

## Setup Instructions

### Prerequisites
- Python 3.x
- Pip

### Install Dependencies
You can set up the environment and install the required dependencies using:
```bash
pip install -r requirements.txt
