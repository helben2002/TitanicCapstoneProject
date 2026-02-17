from django.db import models

class Prediction(models.Model):
    name = models.CharField(max_length=255)

    passenger_class = models.IntegerField()
    sex = models.CharField(max_length=10)
    age = models.FloatField()

    sibling_spouse_count = models.IntegerField()
    parent_child_count = models.IntegerField()

    fare = models.FloatField()
    embarked_port = models.CharField(max_length=1)

    predicted_survival = models.BooleanField()
    probability = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} → {self.predicted_survival}"
