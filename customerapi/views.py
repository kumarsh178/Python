from django.shortcuts import render # type: ignore
from rest_framework import viewsets # type: ignore
from customerapi.models import Customer
from customerapi.serializers import CustomerSerializer
from rest_framework.decorators import action  # type: ignore
from rest_framework.response import Response # type: ignore

#employee viewSet
class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer