# ------------------------------------------------------------
import joblib
import pandas as pd
from pathlib import Path

from ml.titanic_features import (
    rename_columns,
    impute_missing,
    feature_engineer,
    encode_features,
)


# ------------------------------------------------------------

#Paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models/titanic_model.pkl"

# ------------------------------------------------------------

# # Load model
# model = joblib.load(MODEL_PATH)

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
def predict_passenger(data: dict, model):
    
    # Load data
    df = pd.DataFrame([data])

    # Apply preprocessing
    df = prepare_features(df)
    df = prepare_model_data(df)


    # Align columns with training
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)


    # Predict
    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    return prediction, probability



if __name__ == "__main__":
    sample = {
    "PassengerId": 999,
    "Name": "Smith, Mr. John",
    "Pclass": 3,
    "Sex": "male",
    "Age": 25,
    "SibSp": 0,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked": "S"
}
    print(predict_passenger(sample))