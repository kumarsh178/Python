import os
import django
os.environ['DJANGO_SETTINGS_MODULE' ] = 'secondproject.settings'
django.setup()
from home.models import Customer,CustomerFather
from home.documents import CustomerDocument
from faker import Faker

fake = Faker()

#customer = Customer.objects.get(id = "59")
#customer.email = "njopooooo@gmail.com"
#customer.save()

#To update the documenst means elastic search index
#CustomerDocument().update(customer)

#CustomerDocument().delete(id = "59")

customerall = Customer.objects.all()
customerFather = CustomerFather.objects.all()
for customerF in customerFather:
    customer = Customer.objects.get(id = customerF.id)
    customer.father_name = customerF
    customer.save()
