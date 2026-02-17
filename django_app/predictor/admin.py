from django.contrib import admin
from .models import Prediction

# Register your models here.

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "passenger_class",
        "sex",
        "age",
        "fare",
        "embarked_port",
        "predicted_survival",
        "probability",
    )

    list_filter = (
        "predicted_survival",
        "sex",
        "passenger_class",
        "embarked_port",
    )

    ordering = ("-created_at",)