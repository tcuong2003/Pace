from django.urls import path
from . import views

app_name = 'pace_consulting'

urlpatterns = [
    path('', views.pace_consulting_form, name='pace_consulting_form'),
]
