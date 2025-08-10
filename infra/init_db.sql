CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    temperature_celsius NUMERIC(5,2),
    windspeed_kph NUMERIC(5,2),
    weather_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_weather_timestamp
    ON weather_data (timestamp);
