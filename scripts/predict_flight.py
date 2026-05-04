import pandas as pd
from model import train_model

# implement a user input method
def get_user_input():
    print("Enter flight information:\n")

    # ask the user for month input
    month_input = int(input("Month (1-12): "))

    print("\nDay of week:")
    print("0 = Monday, 1 = Tuesday, ..., 6 = Sunday")
    
    # ask the user for day input
    day_input = int(input("Enter day of week: "))
    
    # ask the user for departure output input
    dep_hour_input= int(input("\nDeparture hour (0-23): "))

    # ask the user for carrier information
    carrier_input = input("\nAirline code (UA, AA, DL, etc.): ").upper()
    
    # ask the user for origin airport information
    origin_airport_input = input("Origin airport (ex: SFO): ").upper()
    
    # ask the user for destination airport information
    destination_airport_input = input("Destination airport (ex: LAX): ").upper()

    # print available weather condition options in the terminal for the user
    print("\nWeather condition:")
    print("1 = Clear")
    print("2 = Rain")
    print("3 = Fog")
    print("4 = Storm")
    print("5 = Snow")
    
    # ask the user for weather information
    weather_choice_input = int(input("Choose weather type: "))

    # set the default values
    precipitation = 0
    avg_temp = 70
    avg_wind_speed = 6
    fog = 0
    heavy_fog = 0
    thunder = 0
    hail = 0
    smoke_or_haze = 0

    # adjust the values based on weather type
    if weather_choice_input == 2:  # rain
        precipitation = 0.5
    elif weather_choice_input == 3:  # fog
        fog = 1
    elif weather_choice_input == 4:  # storm
        precipitation = 1.0
        thunder = 1
        avg_wind_speed = 15
    elif weather_choice_input == 5:   # snow
        precipitation = 0.8
        avg_temp = 30
        avg_wind_speed = 10

    return pd.DataFrame([{
        "MONTH": month_input,
        "DAY_OF_WEEK": day_input,
        "DEP_HOUR": dep_hour_input,
        "OP_CARRIER": carrier_input,
        "ORIGIN": origin_airport_input,
        "DEST": destination_airport_input,
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
    # train model
    model = train_model(return_model=True)

    sample_flight = get_user_input()    # get user input
    
    # make the predictions and calculate probability
    prediction = model.predict(sample_flight)[0]
    probability = model.predict_proba(sample_flight)[0][1]
    
    # to handle the print statements, so what the user sees on the terminal
    print("\nPrediction Result:")

    if prediction == 1:
        print("This flight is likely to be delayed.")
    else:
        print("This flight is not likely to be delayed.")

    print(f"Delay probability: {probability:.2%}")


if __name__ == "__main__":
    main()