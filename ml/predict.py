# ------------------------------------------------------------
import joblib
import pandas as pd
from pathlib import Path

from titanic_features import (
    rename_columns,
    impute_missing,
    feature_engineer,
    encode_features,
)


# ------------------------------------------------------------

#Paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models/titanic_model.pkl"
TEST_PATH = BASE_DIR / "data/raw/test.csv"
SUBMISSION_PATH = BASE_DIR / "submissions/submission.csv"

# ------------------------------------------------------------

# Feature preparation
def prepare_features(df):
    df = rename_columns(df)
    df = impute_missing(df)
    df = feature_engineer(df)
    df = encode_features(df)
    return df


def prepare_model_data(df):
    keep = ['passenger_class','is_female']

    keep += [
        c for c in df.columns 
        if c.startswith((
        'title_','fare_group_','age_group_','family_group_','embarked_port_'
        ))
    ]

    return df[keep].copy()

# ------------------------------------------------------------

# Prediction pipeline
def predict():
    # Load model and data
    model = joblib.load(MODEL_PATH)
    print(model)
    df_test = pd.read_csv(TEST_PATH)

    # Save PassengerId BEFORE processing
    passenger_ids = df_test["PassengerId"].copy()

    # Apply preprocessing
    df_test = prepare_features(df_test)
    df_test = prepare_model_data(df_test)


    # Align columns with training
    df_test = df_test.reindex(columns=model.feature_names_in_, fill_value=0)


    # Predict
    predictions = model.predict(df_test)

    # Create submission file
    submission = pd.DataFrame({
        "PassengerId": passenger_ids,
        "Survived": predictions
    })
    submission.to_csv(SUBMISSION_PATH, index=False)


if __name__ == "__main__":
    predict()