from rest_framework import serializers # type: ignore
from django.contrib.auth.models import User

# create serializsers here
class UserSerializser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username', 'password')
    def create (self, validated_data):
        user= User.objects.create(username= validated_data['username'])
        #set password method to hash password
        user.set_password(validated_data['password'])
        user.save()
        return user