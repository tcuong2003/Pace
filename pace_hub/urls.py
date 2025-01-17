from django.urls import path
from . import views

app_name = 'pace_hub'

urlpatterns = [
    path('', views.pace_hub_form, name='pace_hub_form'),
]
