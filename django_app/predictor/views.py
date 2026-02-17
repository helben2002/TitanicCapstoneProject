from django.shortcuts import render
from django.utils import timezone
from datetime import datetime

from .forms import PassengerForm
from .models import Prediction
from .ml_service import TitanicPredictionService

prediction_service = TitanicPredictionService()

from ml.predict_service import predict_passenger


def home(request):
    return render(request, 'predictor/home.html')


def history(request):
    # TODO: fetch predictions from database later

    predictions = Prediction.objects.order_by('-created_at')[:20]

    return render(request, 'predictor/history.html', {
        'predictions': predictions
    })


def predict_view(request):
    prediction = None
    probability = None

    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data


            #  get prediction from service
            prediction, probability = prediction_service.predict(data)
            probability_percent = probability * 100

            # save to database
            Prediction.objects.create(
                name=data['name'],
                passenger_class=data['passenger_class'],
                sex=data['sex'],
                age=data['age'],
                sibling_spouse_count=data['sibling_spouse_count'],
                parent_child_count=data['parent_child_count'],
                fare=data['fare'],
                embarked_port=data['embarked_port'],
                predicted_survival=prediction,
                probability=probability,
                created_at=timezone.now()
            )

            

    else:
        form = PassengerForm()

    return render(request, "predictor/predict.html", {
        "form": form,
        "result": prediction,
        "probability":  probability_percent 
        }
    )
