from django.shortcuts import render
import random
from home.rabbitmq import publish_message, publish_message_bylocal_rabbitmq
from faker import Faker

fake = Faker()
# Create your views here.
def index(request):
    users = []
    for _ in range(100):
        users.append({
            "Name": fake.name(),
            "Email": fake.email(),
            "Gender": random.choice(["Male", "Female"]),
            "Mobile": fake.phone_number(),
            "Address": fake.address()
        })
    message = f"This is the demo message - {random.randint(0, 100)}"
    #publish_message(users)
    publish_message_bylocal_rabbitmq(users)
    return render(request, 'index.html')