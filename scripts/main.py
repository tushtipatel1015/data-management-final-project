import pandas as pd
from model import train_model
from predict_flight import get_user_input

def main():
    print("=== Flight Delay Prediction System ===\n")

    # train model from model.py
    model = train_model(return_model=True)

    # get user input from predict_flight.py
    sample_flight = get_user_input()

    # make prediction
    prediction = model.predict(sample_flight)[0]
    probability = model.predict_proba(sample_flight)[0][1]

    # results
    print("\n=== Prediction Result ===")

    if prediction == 1:
        print("This flight is likely to be delayed.")
    else:
        print("This flight is not likely to be delayed.")

    print(f"Delay probability: {probability:.2%}")

    print("\nThank you for using the Flight Delay Predictor!")

if __name__ == "__main__":
    main()