from django.shortcuts import render # type: ignore
from rest_framework.views import APIView # type: ignore
from customerapi.serializers import UserSerializser
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework.response import Response # type: ignore
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.
class RegisterUser(APIView):
    def post(self, request):
        serializer=UserSerializser(data=request.data)

        if not serializer.is_valid():
            return Response({
                'status':404,
                'errors':serializer.errors,
                'message':"something went wrong"
            })
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj, _= Token.objects.get_or_create(user=user)
        return Response({
                'status':200,
                'payload':serializer.data,
                'token':str(token_obj)
            })
