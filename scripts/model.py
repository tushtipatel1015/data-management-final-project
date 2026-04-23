# logistic regression model
# used to model the probablity of flight delays based on flight data and weather conditions
# another reason we selected it is because it is well suited for binary classifying (either delay or no delay) 
# and also becasue results are easily interpretable and distinguishable
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


def train_model():
    # load merged dataset
    df = pd.read_csv("data/cleaned/merged_data.csv")

    # make sure target is numeric
    df["IS_DELAYED"] = pd.to_numeric(df["IS_DELAYED"], errors="coerce")

    # drop rows missing target
    df = df.dropna(subset=["IS_DELAYED"])

    # choose features that are available before flight arrival
    # avoid leakage: do NOT use ARR_DELAY, delay-cause columns, etc
    # the following cols are what are realistically known prior to a delay
    # leads to more realistic results as opposed to using already present delay data
    feature_cols = [
        "MONTH",
        "DAY_OF_WEEK",
        "DEP_HOUR",
        "OP_CARRIER",
        "ORIGIN",
        "DEST",
        "DISTANCE",
        "precipitation",
        "avg_temp",
        "avg_wind_speed",
        "fog",
        "heavy_fog",
        "thunder",
        "hail",
        "smoke_or_haze"
    ]

    X = df[feature_cols].copy()
    y = df["IS_DELAYED"].astype(int)

    # separate categorical and numeric columns
    categorical_features = ["OP_CARRIER", "ORIGIN", "DEST"]

    numeric_features = [
        "MONTH",
        "DAY_OF_WEEK",
        "DEP_HOUR",
        "DISTANCE",
        "precipitation",
        "avg_temp",
        "avg_wind_speed",
        "fog",
        "heavy_fog",
        "thunder",
        "hail",
        "smoke_or_haze"
    ]

    # preprocessing for numeric data
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")), # missing data will be filled with median value as it is less skewed than by average
        ("scaler", StandardScaler()) # rescales numbers so model isn't dominated by fluctuating numbers. also helps with accuaracy
    ])

    # preprocessing for categorical data
    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")), # fills missing values with mode
        ("onehot", OneHotEncoder(handle_unknown="ignore")) # then converts categories to numeric for model
    ])

    # combine preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    # build model pipeline
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])

    # split data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2, # 20% for testing, so 80% used for training
        random_state=10,
        stratify=y # this makes sure that the amount of delayed flights in both sets of data are the same proportion (avoiding bias and skewed data)
    )

    # training our model
    # some patterns our model will learn:
    #   - evening flight delays vs morning flight delays
    #   - if precipitation (like rain) increases risk of delay
    #   - do certain airlines cause more delays
    model.fit(X_train, y_train)

    # predictions from our model
    y_pred = model.predict(X_test)

    # evaluating our model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)

    # print results
    print("Model: Logistic Regression")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")
    print("\nConfusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # save results to a text file
    os.makedirs("data/outputs/model_results", exist_ok=True)

    with open("data/outputs/model_results/model_results.txt", "w") as f:
        f.write("Model: Logistic Regression\n")
        f.write(f"Accuracy:  {accuracy:.4f}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall:    {recall:.4f}\n")
        f.write(f"F1 Score:  {f1:.4f}\n\n")
        f.write("Confusion Matrix:\n")
        f.write(str(cm))
        f.write("\n\nClassification Report:\n")
        f.write(classification_report(y_test, y_pred, zero_division=0))

    print("\nResults saved to data/outputs/model_results/model_results.txt")


if __name__ == "__main__":
    train_model()