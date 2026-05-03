# Flight Delay Prediction System (SFO)
Data Management Final Project

Group Members: Tushti Patel (tdp80) & Kashish Patel (kdp137)

## Overview
This project analyzes historical flight and weather data to understand and predict flight delays at **San Francisco International Airport (SFO)**.  

While most flight tracking tools only show delays after they happen, our system aims to:
- Identify patterns in delays  
- Analyze how time and weather affect flights  
- Predict whether a flight is likely to be delayed before it happens  

## Features
- Data cleaning and preprocessing of large flight datasets  
- Integration of weather (climate) data  
- Storage using a SQLite database  
- Exploratory data analysis and visualizations  
- Machine learning model to predict delays  
- Interactive prediction system for user input  

## How It Works

The project follows a complete data pipeline:

1. **Clean Flight Data**
   - Filters flights to only include SFO
   - Creates features like `IS_DELAYED`, `MONTH`, `DEP_HOUR`

2. **Clean Weather Data**
   - Formats climate data (temperature, precipitation, wind, etc.)
   - Handles missing values and converts data types

3. **Merge Data**
   - Combines flight and weather data using date

4. **Database Setup**
   - Stores cleaned data in SQLite for structured access

5. **Analysis**
   - Generates visualizations showing:
     - delays by month
     - delays by departure hour
     - effects of weather conditions

6. **Machine Learning**
   - Trains a logistic regression model to predict delays

7. **Prediction System**
   - Takes user input and outputs delay prediction + probability

## Machine Learning Model

- **Model Used:** Logistic Regression  
- **Goal:** Predict whether a flight is delayed (>15 minutes)  

### Features Used:
- Month, day of week, departure hour  
- Airline, origin, destination  
- Weather conditions (temperature, precipitation, wind, etc.)  

### Important Design Choices:
- Avoided **data leakage** by excluding arrival delay and delay-cause columns  
- Handled **class imbalance** 

## Model Performance
- Accuracy: ~60%
- Recall: ~57% (ability to detect delayed flights)
- F1 Score: ~0.40
- This model **prioritizes identifying delays** over maximizing accuracy, making it more useful in real-world scenarios.

## How to Run
1. Install Dependencies
    pip install pandas scikit-learn matplotlib
2. Run Data Pipeline (in order)
    python3 scripts/clean_flights.py
    python3 scripts/clean_weather.py
    python3 scripts/merge_data.py
    python3 scripts/create_database.py
3. Run Analysis
    python3 scripts/analysis.py
4. Train Model
    python3 scripts/model.py
5. Run Prediction System
    python3 main.py

### Example Output
**Input:**
- Month: 4 (April)
- Day of week: 2 (Wednesday)
- Departure hour: 13 (1 PM)
- Airline: DL (Delta)
- Origin: SFO
- Destination: LAX
- Weather: Storm (4)

Prediction Result:
This flight is likely to be delayed.
Delay probability: 68.25%