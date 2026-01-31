from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from .views import *

urlpatterns = [
    path('customerapi/', RegisterUser.as_view()),
]
