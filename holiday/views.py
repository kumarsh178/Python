from django.shortcuts import render
from .models import Places, PapularDestinations, Trips, Testimonials, Subscribers
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    """place1=Places()
    place1.name= "Mumbai"
    place1.img="1.png"
    place1.days= 5
    place1.review= False
    place1.desc= "The City That Never Sleeps"
    place1.price = "550"

    place2=Places()
    place2.name= "Hyderabad"
    place2.img = "2.png"
    place2.days= 4
    place2.review= True
    place2.desc= "First Biryani, Then Sherwani"
    place2.price = "650"

    place3=Places()
    place3.name= "Delhi"
    place3.img= "3.png"
    place3.days= 6
    place3.review= True
    place3.desc= "The People Of Heart"
    place3.price = "950"

    place4=Places()
    place4.name= "Kolkata"
    place4.img="4.png"
    place4.days= 7
    place4.review= True
    place4.desc= "The Worship City"
    place4.price = "360"

    place5=Places()
    place5.name= "Varansi"
    place5.img = "5.png"
    place5.days= 4
    place5.review= False
    place5.desc= "The Mahadev City"
    place5.price = "730"

    place6=Places()
    place6.name= "Nainital"
    place6.img= "6.png"
    place5.days= 9
    place6.review= False
    place6.desc= "The City Of Hills"
    place6.price = "1150"

    places = [place1, place2, place3, place4, place5, place6]
    """
    places = Places.objects.all()
    popularDestinations = PapularDestinations.objects.filter(is_popular=True)
    trips = Trips.objects.filter(is_home=True)
    testimonials = Testimonials.objects.filter(is_home=True)
    return render(request, "index.html", {"places":places,"popularDestinations":popularDestinations, "trips":trips, "testimonials":testimonials })

def destinations(request):
    places = Places.objects.all()
    return render(request, "destinations.html", {"places":places})

def user_subscribe(request):
    if(request.POST['email'] != ""):
        email = request.POST['email']
        isEmailExist = Subscribers.objects.filter(email=email).exists()
        if(isEmailExist == False):
            subscribe = Subscribers()
            subscribe.email = request.POST['email']
            subscribe.is_subscribe = True
            subscribe.save()
            data = {'msg':"User Subscribed Successfully!!"}
        else:
            data = {'msg':"Email is already exist!!"}
    return HttpResponse(json.dumps(data), content_type="application/json")
