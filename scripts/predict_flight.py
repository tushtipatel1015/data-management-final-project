import pandas as pd
from model import train_model

def get_user_input():
    print("Enter flight information:")

    sample = {
        "MONTH": int(input("Month (1-12): ")),
        "DAY_OF_WEEK": int(input("Day of week (0=Mon, 6=Sun): ")),
        "DEP_HOUR": int(input("Departure hour (0-23): ")),
        "OP_CARRIER": input("Airline code (ex: UA, AA, DL): ").upper(),
        "ORIGIN": input("Origin airport code (ex: SFO): ").upper(),
        "DEST": input("Destination airport code (ex: LAX): ").upper(),
        "DISTANCE": float(input("Distance in miles: ")),
        "precipitation": float(input("Precipitation: ")),
        "avg_temp": float(input("Average temperature: ")),
        "avg_wind_speed": float(input("Average wind speed: ")),
        "fog": int(input("Fog? (1=yes, 0=no): ")),
        "heavy_fog": int(input("Heavy fog? (1=yes, 0=no): ")),
        "thunder": int(input("Thunder? (1=yes, 0=no): ")),
        "hail": int(input("Hail? (1=yes, 0=no): ")),
        "smoke_or_haze": int(input("Smoke or haze? (1=yes, 0=no): "))
    }

    return pd.DataFrame([sample])


def main():
    model = train_model(return_model=True)

    sample_flight = get_user_input()

    prediction = model.predict(sample_flight)[0]
    probability = model.predict_proba(sample_flight)[0][1]

    print("\nPrediction Result:")

    if prediction == 1:
        print("This flight is likely to be delayed.")
    else:
        print("This flight is not likely to be delayed.")

    print(f"Delay probability: {probability:.2%}")


if __name__ == "__main__":
    main()