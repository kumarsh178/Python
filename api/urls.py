from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
