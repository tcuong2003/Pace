from django.urls import path
from . import views

app_name = 'gioi_thieu'

urlpatterns = [
    path('', views.gioi_thieu_form, name='gioi_thieu_form'),
]
