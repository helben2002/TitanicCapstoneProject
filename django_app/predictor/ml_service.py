import joblib
import pandas as pd
from pathlib import Path

from ml.predict_service import predict_passenger

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_PATH = BASE_DIR / "ml/models/titanic_model.pkl"

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
        prediction, probability = predict_passenger(raw, model)

        return prediction, probability