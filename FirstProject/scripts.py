import os
import django
os.environ['DJANGO_SETTINGS_MODULE' ] = 'FirstProject.settings'
django.setup()
from home.models import Author, Book, Products, Customer
from employee.models import Employee
from faker import Faker

fake = Faker()

def createBulkAuthor(number):
    authors = []
    for i in range(number):
        author = Author(author_name = fake.name())
        authors.append(author)
    Author.objects.bulk_create(authors)
def deleteBulkAuthor():
    Author.objects.all().delete()
#created = createBulkAuthor(100)
#deleteAuthor = deleteBulkAuthor()
def createCustomer():
    try:

        Customer.objects.create(
            name = "CB",
            email="cb123@yopmail.com",
            phone="8010335187",
            city="ghaziabad",
            age=20
        )
    except django.db.utils.IntegrityError:
        print("Customer age should more than 18")

#createCustomer()
def createEmployee(number):
    emps = []
    for i in range(number):
        emp = Employee(emp_name = fake.name(), emp_email=fake.email(), is_deleted=True)
        emps.append(emp)
    Employee.objects.bulk_create(emps)
createEmployee(10)