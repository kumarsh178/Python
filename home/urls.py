from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from .views import *

urlpatterns = [
    #path('home', home, name='home'),
    path('create_customer', post_customer, name='post_customer'),
    path('get_all_customer', get_all_customer, name='get_all_customer'),
    path('get_customer/<int:pk>/', get_customer, name='get_customer'),
    path('update_customer/<int:pk>/', update_customer, name='update_customer'),
    path('delete_customer/<int:pk>/', delete_customer, name='delete_customer'),
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>/', CustomerList.as_view())
]
