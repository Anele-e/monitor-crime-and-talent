from fastapi import FastAPI
from sqlalchemy import create_engine
import os


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/health")
def health():
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        return {"status": "ok"}

@app.get("/stations/geojson")
async def fetch_data():
    # Logic to fetch data from the database
    return {"message": "Data fetched successfully"}

@app.get("/stations/geojson")
async def fetch_data_by_crime_group(crime_group: str = None):
    # Logic to fetch data from the database based on crime group
    return {"message": f"Data fetched successfully for crime group: {crime_group}"}

@app.get("/stations/{station_name}")
async def fetch_data_by_station(station_name: str):
    # Logic to fetch data from the database based on station name
    return {"message": f"Data fetched successfully for station: {station_name}"}

# school's inside the station area and their pass rate and stuff
@app.get("/stations/{station_name}/schools")
async def fetch_schools_by_station(station_name: str):
    # Logic to fetch schools data from the database based on station name
    return {"message": f"Schools data fetched successfully for station: {station_name}"}

#Search and Filtering
@app.get("/stations/search")
async def search_stations(query: str):
    # Logic to search stations based on query
    return {"message": f"Stations found for query: {query}"}

@app.get("/stations/top")
async def fetch_top_stations(crime_group: str = "", limit: int = 10):
    # Logic to fetch top stations based on crime group and limit
    return {"message": f"Top stations fetched successfully for crime group: {crime_group} with limit: {limit}"}