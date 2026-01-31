from django.urls import path
from .views import home

urlpatterns = [
    path('home1', home, name='home'),
]
