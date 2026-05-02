import pandas as pd
from model import train_model


def get_user_input():
    print("Enter flight information:\n")

    # getting flight date and time
    month = int(input("Month (1-12): "))

    print("\nDay of week:")
    print("0 = Monday, 1 = Tuesday, ..., 6 = Sunday")
    day_of_week = int(input("Enter day of week: "))

    dep_hour = int(input("\nDeparture hour (0-23): "))

    # specific airport and airline information
    carrier = input("\nAirline code (UA, AA, DL, etc.): ").upper()
    origin = input("Origin airport (ex: SFO): ").upper()
    dest = input("Destination airport (ex: LAX): ").upper()

    # getting weather conditions that user currently sees
    # which will be used to make a prediction
    print("\nWeather condition:")
    print("1 = Clear")
    print("2 = Rain")
    print("3 = Fog")
    print("4 = Storm")
    print("5 = Snow")

    weather_choice = int(input("Choose weather type: "))

    #default values
    precipitation = 0
    avg_temp = 60
    avg_wind_speed = 5
    fog = 0
    heavy_fog = 0
    thunder = 0
    hail = 0
    smoke_or_haze = 0

    # map weather to model features
    #   basically setting values to predict delay
    if weather_choice == 2:  # rain
        precipitation = 0.5
    elif weather_choice == 3:  # fog
        fog = 1
    elif weather_choice == 4:  # storm
        precipitation = 1.0
        thunder = 1
        avg_wind_speed = 15
    elif weather_choice == 5:   # snow
        precipitation = 0.8
        avg_temp = 30
        avg_wind_speed = 10

    return pd.DataFrame([{
        "MONTH": month,
        "DAY_OF_WEEK": day_of_week,
        "DEP_HOUR": dep_hour,
        "OP_CARRIER": carrier,
        "ORIGIN": origin,
        "DEST": dest,
        "DISTANCE": 1000,  # default (since user won't know/too specific to user) - we just calculated the average to be around 1000 mi
        "precipitation": precipitation,
        "avg_temp": avg_temp,
        "avg_wind_speed": avg_wind_speed,
        "fog": fog,
        "heavy_fog": heavy_fog,
        "thunder": thunder,
        "hail": hail,
        "smoke_or_haze": smoke_or_haze
    }])


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