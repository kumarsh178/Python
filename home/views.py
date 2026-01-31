from django.shortcuts import render # type: ignore
from rest_framework.views import APIView
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from home.serializers import CustomerSerializer
from customerapi.models import Customer
from rest_framework import status # type: ignore

# Create your views here.

@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response(
            {
            "status":200,
            "message": "Hello, world!"
            }
        )
    elif request.method == 'POST':
        return Response(
            {
            "status":200,
            "message": "Hello,POST world!"
            }
        )
    elif request.method == 'PATCH':
         return Response(
            {
            "status":200,
            "message": "Hello,PATCH world!"
            }
        )
    else:
        return Response(
            {
            "status":200,
            "message": "Invalid Method"
            }
        )
@api_view(['POST'])
def post_customer(request):
    try:
        data=request.data
        serializer = CustomerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'status': True,
            'message':'Success Data',
            'data':serializer.data
            })
        return Response({
            'status': False,
            'message':'Invalid Data',
            'data':serializer.error
        })
    except Exception as e:
        print(e)
    return Response({
        'status':False,
        'message':'Something Went Wrong'
    })

@api_view(['GET'])
def get_customer(request, pk):
    try:
        customer=Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response({
                'status': True,
                'message':'Get Data',
                'data':serializer.data
                })
    except Customer.DoesNotExist:
        return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Item Not Found'
                })

@api_view(['PUT'])
def update_customer(request, pk):
    try:
        customer=Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    'status': True,
                    'message':f'Updated Data with {pk}',
                    'data':serializer.data
                    })
        else:
            return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message':f'Updated Data with {pk}',
                    'data':serializer.errors
                })
    except Customer.DoesNotExist:
        return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Item Not Found'
                })
@api_view(['get'])
def get_all_customer(request):
    try:
        customer=Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response({
                'status': True,
                'message':'All Data Data',
                'data':serializer.data
                })
    except Exception as e:
        return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Something Went Wrong'
                })
@api_view(['DELETE'])
def delete_customer(request, pk):
    try:
        customer=Customer.objects.get(pk=pk)
        customer.delete()
        return Response({
                'status': True,
                'message':f'Data Deleted With {pk}'
                })
    except Customer.DoesNotExist:
        return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Item Not Found'
                })

#class based view
class CustomerList(APIView):
    def get(self, request, pk=None):
            try:
                if not pk:
                    customer=Customer.objects.all()
                    serializer = CustomerSerializer(customer, many=True)
                    return Response({
                            'status': True,
                            'message':'All Data Data',
                            'data':serializer.data
                            })
                else:
                    customer=Customer.objects.get(pk=pk)
                    serializer = CustomerSerializer(customer)
                    return Response({
                    'status': True,
                    'message':'Get Data',
                    'data':serializer.data
                    })
            except Customer.DoesNotExist:
                return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Item Not Found'
                })

    def post(self, request):
            try:
                data=request.data
                serializer = CustomerSerializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                    'status': True,
                    'message':'Success Data',
                    'data':serializer.data
                    })
                return Response({
                    'status': False,
                    'message':'Invalid Data',
                    'data':serializer.error
                })
            except Exception as e:
                print(e)
                return Response({
                    'status':False,
                    'message':'Something Went Wrong'
                })
    def put(self, request, pk):
            try:
                customer=Customer.objects.get(pk=pk)
                serializer = CustomerSerializer(customer, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                            'status': True,
                            'message':f'Updated Data with {pk}',
                            'data':serializer.data
                            })
                else:
                    return Response({
                            'status': status.HTTP_400_BAD_REQUEST,
                            'message':f'Updated Data with {pk}',
                            'data':serializer.errors
                        })
            except Customer.DoesNotExist:
                return Response({
                    'status': status.HTTP_404_NOT_FOUND,
                    'message':'Item Not Found'
                    })
    def delete(self, request, pk):
        try:
            customer=Customer.objects.get(pk=pk)
            customer.delete()
            return Response({
                    'status': True,
                    'message':f'Data Deleted With {pk}'
                    })
        except Customer.DoesNotExist:
            return Response({
                    'status': status.HTTP_404_NOT_FOUND,
                    'message':'Item Not Found'
                    })
