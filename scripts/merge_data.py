import pandas as pd

def merge_data():
    flights = pd.read_csv("data/cleaned/cleaned_flights.csv")
    weather = pd.read_csv("data/cleaned/Cleaned_SFO_2018_Climate.csv")

    flights["FL_DATE"] = pd.to_datetime(flights["FL_DATE"], errors="coerce")
    weather["date"] = pd.to_datetime(weather["date"], errors="coerce")

    merged = flights.merge(
        weather,
        left_on="FL_DATE",
        right_on="date",
        how="left"
    )

    merged.to_csv("data/cleaned/merged_data.csv", index=False)

    print("Merged dataset saved to data/cleaned/merged_data.csv")
    print(f"Rows: {len(merged)}")
    print(f"Columns: {len(merged.columns)}")
    print(merged.head())

if __name__ == "__main__":
    merge_data()