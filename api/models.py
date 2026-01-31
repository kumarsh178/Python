from django.db import models

# Create your models here.

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100, choices=(
        ("it","IT"),
        ("non_id","Non It"),
        ("mobile_phones",'Mobile Phones')
    ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    # this is also use to decide which attribute will display in dropdown
    def __str__(self):
        return self.name
#employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    about=models.TextField()
    position=models.CharField(choices=(
        ("sd","Software Developer"),
        ("manager","Manager"),
        ('pl',"Project Leader")
    ), max_length=100)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

