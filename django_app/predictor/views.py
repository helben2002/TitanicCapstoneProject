from django.shortcuts import render
from .forms import PassengerForm
from ml.predict_service import predict_passenger

def home(request):
    return render(request, 'predictor/home.html', {'message': 'Welcome to the Titanic Survival Predictor!'})


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

    return render(request, "predict.html", {
        "form": form,
        "result": result,
        "probability": probability
    })
