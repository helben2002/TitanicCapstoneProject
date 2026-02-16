from django.urls import path
from . import views

app_name = 'predictor'

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('history/', views.history, name='history'),
]
=======
    path('predict/', views.predict_view, name='predict_view'), 
]

>>>>>>> e6c99aa (data(TITANIC-81): add Django URL routing for prediction view)
