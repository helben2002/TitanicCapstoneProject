from django.shortcuts import render
from datetime import datetime

from .forms import PassengerForm
from ml.predict_service import predict_passenger


def home(request):
    return render(request, 'predictor/home.html')


def history(request):
    # TODO: fetch predictions from database later

    # Dummy data for testing
    predictions = [
        {
            'id': 1,
            'passenger_class': 'First Class',
            'sex': 'Female',
            'age': 22,
            'sibling_spouse_count': 1,
            'parent_child_count': 0,
            'fare': 7.25,
            'embarked_port': 'S',
            'name': 'Heijkenskjöld, Miss Sara',
            'predicted_survival': True,
            'probability': 0.85,
            'created_at': datetime.now()
        },
        {
            'id': 2,
            'passenger_class': 'Second Class',
            'sex': 'Male',
            'age': 35,
            'sibling_spouse_count': 0,
            'parent_child_count': 1,
            'fare': 7.25,
            'embarked_port': 'S',
            'name': 'Heijkenskjöld, Mr. John',
            'predicted_survival': False,
            'probability': 0.80,
            'created_at': datetime.now()
        }
    ]

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
    else:
        form = PassengerForm()

    return render(request, "predictor/predict.html", {
        "form": form,
        "result": result,
        "probability": probability
    })
