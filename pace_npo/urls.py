from django.urls import path
from . import views

app_name = 'pace_npo'

urlpatterns = [
    path('', views.pace_npo_form, name='pace_npo_form'),
]
