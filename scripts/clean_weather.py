import pandas as pd

def clean_weather_data(input_file: str, output_file: str) -> pd.DataFrame:
    # read the climate csv
    df = pd.read_csv(input_file)

    # rename columns to SQL-friendly names
    df = df.rename(columns={
        "STATION": "station_id",
        "NAME": "station_name",
        "DATE": "date",
        "AWND": "avg_wind_speed",
        "PGTM": "peak_gust_time",
        "PRCP": "precipitation",
        "TAVG": "avg_temp",
        "TMAX": "max_temp",
        "TMIN": "min_temp",
        "WDF2": "direction_fastest_2min_wind",
        "WDF5": "direction_fastest_5sec_wind",
        "WSF2": "fastest_2min_wind_speed",
        "WSF5": "fastest_5sec_wind_speed",
        "WT01": "fog",
        "WT02": "heavy_fog",
        "WT03": "thunder",
        "WT05": "hail",
        "WT08": "smoke_or_haze"
    })

    # strip whitespace from cells
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # numeric columns to clean/convert
    numeric_columns = [
        "avg_wind_speed",
        "peak_gust_time",
        "precipitation",
        "avg_temp",
        "max_temp",
        "min_temp",
        "direction_fastest_2min_wind",
        "direction_fastest_5sec_wind",
        "fastest_2min_wind_speed",
        "fastest_5sec_wind_speed",
        "fog",
        "heavy_fog",
        "thunder",
        "hail",
        "smoke_or_haze"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # convert weather flag columns to numerics: 1 if present, 0 if missing
    weather_flag_cols = [
        "fog",
        "heavy_fog",
        "thunder",
        "hail",
        "smoke_or_haze"
    ]

    for col in weather_flag_cols:
        df[col] = df[col].fillna(0).astype(int)

    #save cleaned csv
    df.to_csv(output_file, index=False)

    return df


if __name__ == "__main__":
    cleaned_df = clean_weather_data("SFO_2018_Climate.csv", "Cleaned_SFO_2018_Climate.csv")
    print("Cleaning complete.")
    print(cleaned_df.head())
    print("\nData types:")
    print(cleaned_df.dtypes)
    print(f"\nRows: {len(cleaned_df)}")