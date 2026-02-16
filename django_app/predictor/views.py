from django.shortcuts import render

def home(request):
    return render(request, 'predictor/home.html', {'message': 'Welcome to the Titanic Survival Predictor!'})


def history(request):
    # TODO: fetch predictions
    predictions = []

    return render(request, 'predictor/history.html', {
        'predictions': predictions
    })