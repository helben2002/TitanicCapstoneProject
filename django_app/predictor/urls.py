from django.urls import path
from . import views

app_name = 'predictor'

urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history, name='history'),
    path('predict/', views.predict_view, name='predict_view'), 
]


