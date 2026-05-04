import pandas as pd
import sqlite3
import os

def create_database():
    
    # load cleaned dataset csv files into this one, to help create database
    flights_file = pd.read_csv("data/cleaned/cleaned_flights.csv")
    weather_file = pd.read_csv("data/cleaned/Cleaned_SFO_2018_Climate.csv")
    
    # safety check to ensure database folder exists
    os.makedirs("data/database", exist_ok = True)

    # creating SQLite database connection
    conn = sqlite3.connect("data/database/flights_weather.db")

    # storing as tables in the SQLite database
    flights_file.to_sql("Flights", conn, if_exists="replace", index=False)
    weather_file.to_sql("Weather", conn, if_exists="replace", index=False)

    conn.close()    # close connection once done
    
    # print everything at the end as a confirmation
    print("Database created successfully.")
    print("Tables created:")
    print(" 1. Flights")
    print(" 2. Weather")

if __name__ == "__main__":
    create_database()