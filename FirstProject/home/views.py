from django.shortcuts import render, redirect
from .models import Products,Customer
from django.db.models import Q
from django.http import JsonResponse
from store.models import Store
# Create your views here.
def index(request):
    bmp_id = request.headers.get("bmp")
    store = Store.objects.get(bmp_id = bmp_id)
    data = {
        "status":True,
        "message": "Store Data",
        "Data":{
                "bmp_id":store.bmp_id,
                "store_name":store.store_name
            }
        }
    #return render(request, "index.html", context )
    #print(request.headers)
    return JsonResponse(data)
# Create your views here.
def createProduct(request):
    context = {
        "title":"Create Product"
        }
    return render(request, "create_product.html", context )
def saveProduct(request):
    context = {
        "title":"Create Product"
        }
    product_name = request.POST['product_name']
    upload_file = request.FILES['upload_file']
    Products.objects.create(
        name = product_name,
        product_image = upload_file
    )
    return redirect("/product/create")
def search(request):
    customer = Customer.objects.all()
    search = request.GET.get("search")
    age = request.GET.get("age")
    if search:
        customer = customer.filter(
            Q(name__icontains = search) |
            Q(email__icontains = search) |
            Q(phone__icontains = search) |
            Q(city__icontains = search)
        )
    if age:
        age = int(age)
        if age == 1:
            customer = customer.filter(age__gte = 18, age__lte=20).order_by('age')
        if age == 2:
            customer = customer.filter(age__gte = 20, age__lte=20).order_by('age')
        if age == 3:
            customer = customer.filter(age__gte = 22, age__lte=24).order_by('age')
        if age == 4:
            customer = customer.filter(age__gte = 24, age__lte=100).order_by('age')
    
    context = {
        "customers":customer
        }
    return render(request,"search.html", context)