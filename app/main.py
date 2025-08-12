import requests
import pandas as pd
from sqlalchemy import text
from db import get_engine
import config

def fetch_weather_data():
    """Fetch weather data from API."""
    params = {
        "latitude": config.LATITUDE,
        "longitude": config.LONGITUDE,
        "hourly": "temperature_2m,windspeed_10m",
        "timezone": "UTC"
    }
    response = requests.get(config.WEATHER_API_URL, params=params)
    response.raise_for_status()
    return response.json()

def transform_weather_data(data):
    """Transform API response into DataFrame."""
    hourly = data["hourly"]
    df = pd.DataFrame({
        "timestamp": hourly["time"],
        "temperature_celsius": hourly["temperature_2m"],
        "windspeed_kph": hourly["windspeed_10m"]
    })
    return df

def load_weather_data(df):
    """Load DataFrame into PostgreSQL."""
    engine = get_engine()
    with engine.begin() as conn:
        for _, row in df.iterrows():
            conn.execute(
                text("""
                INSERT INTO weather_data (timestamp, temperature_celsius, windspeed_kph, location)
                VALUES (:timestamp, :temperature_celsius, :windspeed_kph, :location)
                ON CONFLICT (timestamp) DO NOTHING
                """),
                {
                    "timestamp": row["timestamp"],
                    "temperature_celsius": row["temperature_celsius"],
                    "windspeed_kph": row["windspeed_kph"],
                    "location": row["location"]
                }
            )


def transform_weather_data(data):
    """Transform API response into DataFrame."""
    hourly = data["hourly"]
    df = pd.DataFrame({
        "timestamp": hourly["time"],
        "temperature_celsius": hourly["temperature_2m"],
        "windspeed_kph": hourly["windspeed_10m"]
    })
    # Add this line to add location column with fixed value "Peshawar"
    df["location"] = "Peshawar"
    return df


if __name__ == "__main__":
    print("Fetching weather data...")
    data = fetch_weather_data()
    df = transform_weather_data(data)
    print(f"Fetched {len(df)} records.")

    # Save the fetched data to CSV inside your project folder
    df.to_csv("weather_data_sample.csv", index=False)
    print("Data saved to weather_data_sample.csv")

    load_weather_data(df)
    print("Data loaded into database.")
