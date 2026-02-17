from django.shortcuts import render
from datetime import datetime

from .forms import PassengerForm
from ml.predict_service import predict_passenger
from .models import Prediction


def home(request):
    return render(request, 'predictor/home.html')


def history(request):

    predictions = Prediction.objects.order_by("-created_at")

    return render(request, 'predictor/history.html', {
        'predictions': predictions
    })


def predict_view(request):
    result = None
    probability = None

    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # ML prediction
            result, probability = predict_passenger(data)

            # Map form → DB model fields
            db_data = {
                "name": data["Name"],
                "passenger_class": data["Pclass"],
                "sex": data["Sex"],
                "age": data["Age"],
                "sibling_spouse_count": data["SibSp"],
                "parent_child_count": data["Parch"],
                "fare": data["Fare"],
                "embarked_port": data["Embarked"],
            }

            # SAVE TO DATABASE
            Prediction.objects.create(
                **db_data,
                predicted_survival=(int(result) == 1),
                probability=float(probability) if probability is not None else None,
                input_data=data,
            )

    else:
        form = PassengerForm()

    return render(request, "predictor/predict.html", {
        "form": form,
        "result": result,
        "probability": probability
    })