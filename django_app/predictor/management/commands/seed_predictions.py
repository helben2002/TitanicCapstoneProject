from django.core.management.base import BaseCommand
from predictor.models import Prediction


class Command(BaseCommand):
    help = "Seed database with test predictions"

    def handle(self, *args, **kwargs):
        if Prediction.objects.exists():
            self.stdout.write(self.style.WARNING("Predictions already exist — skipping seed"))
            return

        Prediction.objects.create(
            name="Test, Mr One",
            passenger_class=3,
            sex="male",
            age=30,
            sibling_spouse_count=0,
            parent_child_count=0,
            fare=10.5,
            embarked_port="S",
            predicted_survival=False,
            probability=0.22,
            input_data={}
        )

        Prediction.objects.create(
            name="Test, Miss Two",
            passenger_class=1,
            sex="female",
            age=25,
            sibling_spouse_count=0,
            parent_child_count=0,
            fare=100,
            embarked_port="C",
            predicted_survival=True,
            probability=0.95,
            input_data={}
        )

        self.stdout.write(self.style.SUCCESS("Seeded predictions"))