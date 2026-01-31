# Create your tasks here

from celery import shared_task
from faker import Faker
from home.models import Customer
fake = Faker()

@shared_task
def add(x, y):
    print("heloooooooooooo")
    return x + y

@shared_task
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
