from django.db import models

# Create your models here.
class Prediction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    # Form inputs
    name = models.CharField(max_length=100)
    passenger_class = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=10)
    age = models.FloatField()
    sibling_spouse_count = models.PositiveSmallIntegerField()
    parent_child_count = models.PositiveSmallIntegerField()
    fare = models.FloatField()
    embarked_port = models.CharField(max_length=1)

    # Model output
    predicted_survival = models.BooleanField()
    probability = models.FloatField(null=True, blank=True)

    # Save original payload
    input_data = models.JSONField(default=dict, blank=True)


    def __str__(self):
        return f"Prediction {self.predicted_survival} @ {self.created_at:%Y-%m-%d %H:%M}"