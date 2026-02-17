from .models import Prediction

def save_prediction_from_form_data(data, prediction, probability=None):
    return Prediction.objects.create(
        name=data["Name"],
        passenger_class=data["Pclass"],
        sex=data["Sex"],
        age=data["Age"],
        sibling_spouse_count=data["SibSp"],
        parent_child_count=data["Parch"],
        fare=data["Fare"],
        embarked_port=data["Embarked"],
        predicted_survival=bool(prediction),
        probability=probability,
        input_data=data,
    )