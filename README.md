# Weather Data ETL Pipeline with Docker & PostgreSQL

This project is a comprehensive end-to-end **ETL (Extract, Transform, Load) pipeline** designed to fetch real-time weather data from an API, transform and clean the data, and load it into a **PostgreSQL** database. The entire system is containerized using **Docker** to simplify deployment, scalability, and environment management.

---

## Project Overview

The main goal of this project is to build a reliable and reproducible data pipeline that automates the workflow of collecting weather data, transforming it for analysis, and storing it efficiently in a database. This setup is ideal for data engineering learning and real-world applications that require automated data ingestion and processing.

---

## Key Components

- **Dockerfile**: Defines the container image with the required Python environment and dependencies for running the ETL pipeline.
- **docker-compose.yml**: Orchestrates multiple containers including the ETL application and PostgreSQL database, setting up networking and volume persistence.
- **main.py**: The entry point script that triggers the ETL process inside the container.
- **etl.py**: Contains the core ETL logic — extracting data from the weather API, cleaning and transforming it.
- **db.py**: Manages PostgreSQL database connections, schema creation, and data insertion.
- **config/**: (If applicable) Configuration files for API keys, database credentials, and environment variables.
- **requirements.txt**: Lists all Python dependencies required for the project.
- **scripts/**: (Optional) Additional helper scripts for database initialization or data export.
  
---

## How It Works

1. **Extract**  
   The ETL pipeline fetches current weather data from an external API using Python requests or a similar library.

2. **Transform**  
   The raw data is cleaned, filtered, and structured into a format suitable for database insertion. This may include converting units, handling missing values, and normalizing field names.

3. **Load**  
   The processed data is inserted into a PostgreSQL database running inside a Docker container. The database schema is created and managed via `db.py`.

4. **Persistence and Data Access**  
   Docker volumes ensure that the database data persists across container restarts. You can also export the data to CSV for further analysis.

---

## Running the Project

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/weather-etl-pipeline.git
   cd weather-etl-pipeline
