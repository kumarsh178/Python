from rest_framework import serializers # type: ignore
from api.models import Company,Employee

# create serializsers here
class CompanySerializser(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"
        
#employee Serializers
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"

