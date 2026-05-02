def main():
    print("=== Flight Delay Prediction System ===\n")

    # Train and get the model
    model = train_model(return_model=True)

    # Get user input
    sample_flight = get_user_input()

    # Make prediction
    prediction = model.predict(sample_flight)[0]
    probability = model.predict_proba(sample_flight)[0][1]

    # Display results
    print("\n=== Prediction Result ===")

    if prediction == 1:
        print("This flight is likely to be delayed.")
    else:
        print("This flight is not likely to be delayed.")

    print(f"Delay probability: {probability:.2%}")

    print("\nThank you for using the Flight Delay Predictor!")