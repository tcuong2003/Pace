from django.urls import path
from . import views

app_name = 'pace_training'

urlpatterns = [
    path('', views.pace_training_form, name='pace_training_form'),
]
