import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from pathlib import Path

#--------------------------------------------------------------------------
BASE_DIR = Path.cwd()
MODEL_PATH = BASE_DIR / "ml/models/titanic_model.pkl"
#--------------------------------------------------------------------------
# Load
def load_data():
    train_path = BASE_DIR / "ml/data/raw/train.csv"

    df_train = pd.read_csv(train_path)

    return df_train

#--------------------------------------------------------------------------
# Rename columns
def rename_columns(df):
    df = df.copy()
    df.columns = df.columns.str.lower()

    rename_map = {
        'passengerid': 'passenger_id',
        'pclass': 'passenger_class',
        'sibsp': 'sibling_spouse_count',
        'parch': 'parent_child_count',
        'ticket': 'ticket_number',
        'embarked': 'embarked_port'
    }

    return df.rename(columns=rename_map)
#--------------------------------------------------------------------------

# Handle missing values
def impute_missing(df):
    df = df.copy()

    df["embarked_port"] = df["embarked_port"].fillna(df["embarked_port"].mode()[0])

    df["age"] = df["age"].fillna(
        df.groupby(["passenger_class", "sibling_spouse_count", "parent_child_count"])["age"]
        .transform("median")
    )

    df["age"] = df["age"].fillna(df["age"].median())

    return df
#--------------------------------------------------------------------------

# Feature engineering
AGE_BINS = [0, 13, 18, 30, 50, 100]
AGE_LABELS = ['child', 'teenager', 'young_adult', 'adult', 'senior']

FARE_BINS = [0, 16, 30, 1000]
FARE_LABELS = ['low', 'medium', 'high']

FAMILY_SIZE_BINS = [0, 1, 4, 20]
FAMILY_SIZE_LABELS = ['alone', 'small', 'large']


def extract_title(name):
    title = name.str.extract(r',\s*([^\.]+)\.')
    title_map = {'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'}
    title = title.replace(title_map)

    rare = ['Lady','the Countess','Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona']
    title = title.replace(rare, 'other')

    return title


def feature_engineer(df):
    df = df.copy()

    df["age_group"] = pd.cut(df["age"], AGE_BINS, labels=AGE_LABELS)
    df["fare_group"] = pd.cut(df["fare"], FARE_BINS, labels=FARE_LABELS)

    df["family_size"] = df["sibling_spouse_count"] + df["parent_child_count"] + 1
    df["family_group"] = pd.cut(df["family_size"], FAMILY_SIZE_BINS, labels=FAMILY_SIZE_LABELS)

    df["title"] = extract_title(df["name"])

    df["is_female"] = df["sex"].map({"male":0, "female":1})

    return df
#--------------------------------------------------------------------------

# Encoding
def encode_features(df):
    cols = ['title','age_group','fare_group','family_group','embarked_port']

    return pd.get_dummies(df, columns=cols, dtype=int)

#--------------------------------------------------------------------------

# Select model columns
def prepare_model_data(df):
    keep = ['survived','passenger_class','is_female']

    keep += [c for c in df.columns if c.startswith((
        'title_','fare_group_','age_group_','family_group_','embarked_port_'
    ))]

    df_model = df[keep]

    X = df_model.drop('survived', axis=1)
    y = df_model['survived']

    return X, y

#--------------------------------------------------------------------------

# Train model
def train_model(X_train, y_train):
    model = Pipeline([
        ('logreg', LogisticRegression(max_iter=1000))
    ])
    model.fit(X_train, y_train)
    return model

#--------------------------------------------------------------------------

# Evaluate model
def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    cm = confusion_matrix(y_test, preds)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.show()

#--------------------------------------------------------------------------

# Cross validation
def cross_validate(model, X, y):
    scores = cross_val_score(model, X, y, cv=5)
    print("CV mean:", scores.mean())

#--------------------------------------------------------------------------

# Save model
def save_model(model, path):
    joblib.dump(model, path)

#--------------------------------------------------------------------------

# Main pipeline
def main():

    train = load_data()

    train = rename_columns(train)
    train = impute_missing(train)
    train = feature_engineer(train)
    train = encode_features(train)

    X, y = prepare_model_data(train)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)
    cross_validate(model, X, y)
    save_model(model, MODEL_PATH)

#--------------------------------------------------------------------------

if __name__ == "__main__":
    main()
