from rest_framework import serializers # type: ignore
from customerapi.models import Customer

#employee Serializers
class CustomerSerializer(serializers.ModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model=Customer
        #fields is used to define the field which will be used or not
        fields=("name","email","city","phone")
        #exclude keyword to use to exclude some fields
        #exclude=("phone")

