import joblib
import pandas as pd
from pathlib import Path

from ml.titanic_pipeline import prepare_training_data

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "ml/titanic_model.pkl"

class TitanicPredictionService:
    def __init__(self):
        self.model = None

    def _load_model(self):
        if self.model is None:
            self.model = joblib.load(MODEL_PATH)
        return self.model

    def _to_kaggle_schema(self, data: dict):
        return {
            'Pclass': data['passenger_class'],
            'Name': data['name'],
            'Sex': data['sex'],
            'Age': data['age'],
            'SibSp': data['sibling_spouse_count'],
            'Parch': data['parent_child_count'],
            'Fare': data['fare'],
            'Embarked': data['embarked_port']
        }

    def predict(self, form_data):
        model = self._load_model()
        raw = self._to_kaggle_schema(form_data)
        df = pd.DataFrame([raw])
        X, _ = prepare_training_data(df)
        prediction = int(model.predict(X)[0])
        probability = float(model.predict_proba(X)[0][1])

        return prediction, probability