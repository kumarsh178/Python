from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('product/create', views.createProduct, name='createProduct'),
    path('product/save', views.saveProduct, name='saveProduct'),
    path('customer/search', views.search, name='search')
]