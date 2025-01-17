from django.urls import path
from . import views

app_name = 'lien_he'

urlpatterns = [
    path('', views.lien_he_form, name='lien_he_form'),
]
