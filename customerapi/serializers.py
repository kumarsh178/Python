from rest_framework import serializers # type: ignore
from customerapi.models import Customer

#employee Serializers
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model=Customer
        fields="__all__"

