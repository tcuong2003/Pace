from django.urls import path
from . import views

app_name = 'pace_books'

urlpatterns = [
    path('', views.pace_books_form, name='pace_books_form'),
]
