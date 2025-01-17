from django.urls import path
from . import views

app_name = 'tuyen_dung'

urlpatterns = [
    path('', views.tuyen_dung_form, name='tuyen_dung_form'),
]
