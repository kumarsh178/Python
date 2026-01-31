from django.shortcuts import render # type: ignore
from rest_framework import viewsets # type: ignore
from api.models import Company, Employee
from api.serializers import CompanySerializser,EmployeeSerializer
from rest_framework.decorators import action 
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializser
    #details true means you have to pass primary key
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company= Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer= EmployeeSerializer(emps, many=True, context={"request":request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response(
                {
                    'message':"company might not exist"
                }
            )

#employee viewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
