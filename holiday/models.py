from django.db import models

# Create your models here.
class Places(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='places')
    description= models.TextField()
    price= models.IntegerField()
    days= models.IntegerField()
    review= models.BooleanField(default=False)
    car= models.CharField(max_length=100)

class PapularDestinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="destimages")
    num_of_places = models.IntegerField()
    is_popular = models.BooleanField(default=False)
    created_at = models.DateField()
    updated_at = models.DateTimeField()

class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField()
    img = models.ImageField(upload_to="testimonials")
    is_home = models.BooleanField(default=False)

class Trips(models.Model):
    title = models.CharField(max_length=300)
    img = models.ImageField(upload_to="trips")
    trip_date = models.DateField()
    is_home = models.BooleanField()

class Subscribers(models.Model):
    email = models.EmailField()
    is_subscribe = models.BooleanField()

