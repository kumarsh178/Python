import os
import django
os.environ['DJANGO_SETTINGS_MODULE' ] = 'celery_project.settings'
django.setup()
from home.models import Customer
from faker import Faker

fake = Faker()

def createBulkCustomer(number):
    allCust = []
    for i in range(number):
        customer = Customer(
            name = fake.name(),
            email = fake.email(),
            phone = fake.phone_number(),
            city = fake.city(),
            age = fake.random_int(15,80)         
        )
        allCust.append(customer)
    Customer.objects.bulk_create(allCust)
 
createBulkCustomer(15)
 

