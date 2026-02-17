from django.shortcuts import render
from pathlib import Path
from django.utils import timezone
import markdown

from .forms import PassengerForm
from .models import Prediction
from .ml_service import TitanicPredictionService

prediction_service = TitanicPredictionService()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def home(request):
    readme_path = BASE_DIR / "README.md"

    readme_html = ""
    if readme_path.exists():
        text = readme_path.read_text(encoding="utf-8")
        readme_html = markdown.markdown(text)

    return render(request, "predictor/home.html", {
        "readme": readme_html
    })


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
        "probability": probability
    })
