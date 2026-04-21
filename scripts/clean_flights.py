import pandas as pd
import glob
import os

def clean_flights():
    files = glob.glob("split_flights/*.csv")    # find all split flight csv files
    
    if not files:
        print("No files found in split_flights/")
        return
    
    dataframe_list = [] # load and combine all monthly files
    
    for file in files:
        dataframe = pd.read_csv(file)
        dataframe_list.append(dataframe)
    
    flights = pd.concat(dataframe_list, ignore_index = True)
    
    # drop unnamed section data
    flights = flights.drop(columns = ["Unnamed: 27"], errors = "ignore")
    
    # convert date column to datetime
    flights["FL_DATE"] = pd.to_datetime(flights["FL_DATE"], errors = "coerce")
    
    # safety check to ensure that we only consider 
    flights = flights[
        (flights["ORIGIN"] == "SFO") |
        (flights["DEST"] == "SFO")
    ]
    
    flights = flights.dropna(subset = ["FL_DATE"])  # remove rows where date is missing
    
    flights["IS_DELAYED"] = (flights["ARR_DELAY"] > 15).astype(int) # create target columns
    
    # create useful time features
    flights["MONTH"] = flights["FL_DATE"].dt.month
    flights["DAY_OF_WEEK"] = flights["FL_DATE"].dt.dayofweek
    flights["DEP_HOUR"] = flights["CRS_DEP_TIME"] // 100
    
    os.makedirs("data", exist_ok = True)
    flights.to_csv("cleaned_flights.csv", index = False)
    
    print("Cleaned flights file saved to cleaned_flights.csv")
    print(f"Rows: {len(flights)}")
    print(f"Columns: {len(flights.columns)}")
    
if __name__ == "__main__":
    clean_flights()