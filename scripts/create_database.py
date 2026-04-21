import pandas as pd
import sqlite3

def create_database():

    # load cleaned datasets
    flights = pd.read_csv("data/cleaned/cleaned_flights.csv")
    weather = pd.read_csv("data/cleaned/Cleaned_SFO_2018_Climate.csv")

    # create database connection
    conn = sqlite3.connect("data/database/flights_weather.db")

    # write tables into database
    flights.to_sql("Flights", conn, if_exists="replace", index=False)
    weather.to_sql("Weather", conn, if_exists="replace", index=False)

    conn.close()

    print("Database created successfully.")
    print("Tables created:")
    print(" - Flights")
    print(" - Weather")

if __name__ == "__main__":
    create_database()