"""
URL configuration for Website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('pace_training/', include('pace_training.urls')), 
    path('pace_consulting/', include('pace_consulting.urls')), 
    path('pace_books/', include('pace_books.urls')),
    path('pace_npo/', include('pace_npo.urls')),
    path('pace_seminar/', include('pace_seminar.urls')),
    path('pace_hub/', include('pace_hub.urls')),
    path('tuyen_dung/', include('tuyen_dung.urls')),
    path('lien_he/', include('lien_he.urls')),
    path('gioi_thieu/', include('gioi_thieu.urls')),
]
