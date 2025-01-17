from django.urls import path
from . import views

app_name = 'pace_seminar'

urlpatterns = [
    path('', views.pace_seminar_form, name='pace_seminar_form'),
]