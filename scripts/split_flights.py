import pandas as pd
import os

# load original dataset
file_path = "Flight Cancellations and Delays 2018.csv"

# folder where split files will be saved
output_folder = "data/split_flights"
os.makedirs(output_folder, exist_ok=True )

# read the dataset
df = pd.read_csv(file_path)

# convert the date column to datetime
df["FL_DATE"] =pd.to_datetime(df["FL_DATE"])

# split by month
for month, group in df.groupby(df["FL_DATE"].dt.month):
    filename = f"{output_folder}/flights_2018_{month:02d}.csv"
    group.to_csv(filename, index=False)
    print(f"Saved {filename}")