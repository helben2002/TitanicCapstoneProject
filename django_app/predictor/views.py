from django.shortcuts import render
from datetime import datetime

from .forms import PassengerForm
from .models import Prediction
from ml.predict_service import predict_passenger


def home(request):
    return render(request, 'predictor/home.html')


def history(request):
    predictions = Prediction.objects.all().order_by("-created_at")

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
            result, probability = predict_passenger(data)

            Prediction.objects.create(
                name=data["Name"],
                passenger_class=data["Pclass"],
                sex=data["Sex"],
                age=data["Age"],
                sibling_spouse_count=data["SibSp"],
                parent_child_count=data["Parch"],
                fare=data["Fare"],
                embarked_port=data["Embarked"],
                predicted_survival=bool(result),
                probability=probability
            )

    else:
        form = PassengerForm()

    return render(request, "predictor/predict.html", {
        "form": form,
        "result": result,
        "probability": probability
    })
