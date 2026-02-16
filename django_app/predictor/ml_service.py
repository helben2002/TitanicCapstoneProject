import joblib
import pandas as pd
from pathlib import Path

from ml.titanic_pipeline import prepare_training_data

class TitanicPredictionService:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        model_path = base_dir / "ml/titanic_model.pkl"
        self.model = joblib.load(model_path)

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
        raw = self._to_kaggle_schema(form_data)
        df = pd.DataFrame([raw])
        X, _ = prepare_training_data(df)
        prediction = int(self.model.predict(X)[0])
        probability = float(self.model.predict_proba(X)[0][1])

        return prediction, probability