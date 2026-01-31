from django.shortcuts import render
from home.tasks import add, createBulkCustomer
from django.http import JsonResponse
# Create your views here.

def index(request):
    add.delay(10, 5)
    createBulkCustomer.delay(30)
    return JsonResponse({
        "status": True,
        "message":"Task Added"
    })
