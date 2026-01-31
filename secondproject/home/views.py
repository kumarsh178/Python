from django.shortcuts import render, redirect
from .models import Customer
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .documents import CustomerDocument
from elasticsearch_dsl.query import MultiMatch
import logging
logger = logging.getLogger(__name__)

# Create your views here.


@cache_page(60 * 15)
def index(request):
    print("heloooooooooooooooooooo")
    logger.debug("this debugggggg")
    customer = Customer.objects.all()
    logger.debug("this debugggggg")
    search = request.GET.get("search")
    age = request.GET.get("age")
    cache.set("customers", customer, 60*1)
    if search:
        customer = customer.filter(
            Q(name__icontains = search) |
            Q(email__icontains = search) |
            Q(phone__icontains = search) |
            Q(city__icontains = search)
        )
        cache.set("customers", customer, 60*1)
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
        cache.set("customers", customer, 60*1)
    if cache.get("customers"):
        customer = cache.get("customers")
    else:
        cache.set("customers", customer, 60*1)
    logger.debug(f"{customer.count()}")
    context = {
        "customers":customer
        }
    return render(request,"index.html", context)

def customers(request):

    logger.debug("this debugggggg")
    logger.error("error")
    logger.warning("warninggggg")
    customer = Customer.objects.all()
    logger.debug(f"{customer.count()}")

    context = {
        "customers":customer
        }
    return render(request,"customers.html", context)

def customerSearch(request):
    data = {}
    customer = CustomerDocument.search().scan()
    if request.GET.get('search'):
        search = request.GET.get('search')
        # single search on fields it will return the string match in the whole sentence
        """result = CustomerDocument.search().query(
            'match',name = search
        )"""
        #multi match
        """result = CustomerDocument.search().query(
                MultiMatch(query = search, fields=[
                    "name",
                    "email",
                    "phone",
                    "city"
                ]
            )
        ).sort('age')""" #asc 

        """result = CustomerDocument.search().query(
                MultiMatch(query = search, fields=[
                    "name",
                    "email",
                    "phone",
                    "city"
                ]
            )
        ).sort('age')""" # DESC 

        # collapse use for distinct result on specific field
        """result = CustomerDocument.search().query(
                MultiMatch(query = search, fields=[
                    "name",
                    "email",
                    "phone",
                    "city"
                ]
            )
        ).collapse(field = 'age')"""
       
        # fuzziness AUTO means it will search even you will add wrong spelling
        """result = CustomerDocument.search().query(
            'match',name ={
                'query': search,
                'fuzziness': 'AUTO'
            }
        )"""
        print(search)

        #term with multiple value
        """
        search = search.split(",") #Delhi,Mumbai
        result = CustomerDocument.search().query(
               'terms', age = search
            )
        """
        #term with single value
        result = CustomerDocument.search().query(
               'term', age = search
            )
        
        ## extra pagination
        """result = CustomerDocument.search().query(
               'term', age = search
            ).extra(size = 20)"""
        ## extra pagination from to 
        result = CustomerDocument.search().query(
               'term', age = search
            ).extra(from_ = 1, size = 8)
        
        result = result.execute()
        customer = result
        logger.debug(result)
    context = {
        "customers":customer
        }
    return render(request,"customer_search.html", context)