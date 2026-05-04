import pandas as pd
import os

def merge_data():
    
    # load cleaned dataset csv files into this one
    flights_file = pd.read_csv("data/cleaned/cleaned_flights.csv")
    weather_file = pd.read_csv("data/cleaned/Cleaned_SFO_2018_Climate.csv")

    flights_file["FL_DATE"] = pd.to_datetime(flights_file["FL_DATE"], errors="coerce")
    weather_file["date"] = pd.to_datetime(weather_file["date"], errors="coerce")
    
    # merge flight and weather data, on date
    merged = flights_file.merge(
        weather_file,
        left_on="FL_DATE",
        right_on="date",
        how="left"
    )
    
    # safety check to ensure cleaned folder exists
    os.makedirs("data/cleaned", exist_ok = True)
    merged.to_csv("data/cleaned/merged_data.csv", index=False)  # save the merged dataset to merged_data.csv
    
    # print everything at the end as a confirmation
    print("Merged dataset saved to data/cleaned/merged_data.csv")
    print(f"Rows: {len(merged)}")
    print(f"Columns: {len(merged.columns)}")
    print(merged.head())

if __name__ == "__main__":
    merge_data()