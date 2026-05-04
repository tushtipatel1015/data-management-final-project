import pandas as pd
import glob
import os

def clean_flights():
    
    # find all flight files (monthly split)
    files = glob.glob("split_flights/*.csv")
    
    # if not file is found print a message
    if not files:
        print("No files found in split_flights/")
        return
    
    # to combine each monthly file into one dataframe
    flight_dataframe_list = []
    
    for file in files:
        dataframe = pd.read_csv(file)
        flight_dataframe_list.append(dataframe)
    
    flights = pd.concat(flight_dataframe_list, ignore_index = True)
    
    # Step 1: drop extra columns "Unnamed" to prevent unnecessary analysis
    flights = flights.drop(columns = ["Unnamed: 27"], errors = "ignore")
    
    # Step 2: convert flight date to a common datetime format
    flights["FL_DATE"] = pd.to_datetime(flights["FL_DATE"], errors = "coerce")
    
    # only consider flights coming to or going from SFO airport
    flights = flights[
        (flights["ORIGIN"] == "SFO") |
        (flights["DEST"] == "SFO")
    ]
    
    # Step 3: remove rows where the date is missing
    flights = flights.dropna(subset = ["FL_DATE"]) 
    
    # do only if flight arrives more than 15 mins late
    flights["IS_DELAYED"] = (flights["ARR_DELAY"] > 15).astype(int)
    
    # creation of time based features for easier reading of data for analysis and prediction
    flights["MONTH"] = flights["FL_DATE"].dt.month
    flights["DAY_OF_WEEK"] = flights["FL_DATE"].dt.dayofweek
    flights["DEP_HOUR"] = flights["CRS_DEP_TIME"] // 100
    
    # save cleaned flight data in cleaned_flights.csv
    os.makedirs("data/cleaned", exist_ok = True)    # safety check to ensure cleaned folder exists
    flights.to_csv("cleaned_flights.csv", index = False)
    
    print("Cleaned flights file saved to cleaned_flights.csv")
    print(f"Rows: {len(flights)}")
    print(f"Columns: {len(flights.columns)}")
    
if __name__ == "__main__":
    clean_flights()