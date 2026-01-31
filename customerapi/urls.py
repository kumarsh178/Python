from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from customerapi.views import CustomerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
