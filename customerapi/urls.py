from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from customerapi.views import RegisterUser

urlpatterns = [
    path('register', RegisterUser.as_view())
]
