import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from pathlib import Path

from ml.titanic_pipeline import prepare_training_data

#--------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data/raw/train.csv"
MODEL_PATH = BASE_DIR / "models/titanic_model.pkl"
#--------------------------------------------------------------------------

# Load
def load_data():
    train_path = BASE_DIR / "ml/data/raw/train.csv"

    df_train = pd.read_csv(train_path)

    return df_train
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
def save_model(model, path=MODEL_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)

    print(f"Model saved to {path}")
#--------------------------------------------------------------------------

# Train pipeline
def train():
    # Load data
    df = pd.read_csv(DATA_PATH)

    # Preprocess data and get X, y for modeling
    X, y = prepare_training_data(df)
    
    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    
    # Train model
    model = train_model(X_train, y_train)

    #  Evaluate model
    evaluate_model(model, X_test, y_test)

    # Cross validate model
    cross_validate(model, X, y)

    #  Save model
    save_model(model)
#--------------------------------------------------------------------------

if __name__ == "__main__":
    train()