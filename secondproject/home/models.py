from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100, unique=True)
    student_id = models.CharField(max_length=100, null=True, blank=True)
@receiver(post_save, sender=Student)
def save_student(sender, instance, created, **kwargs):
    if created:
        instance.student_id = f"STU-000{instance.id}"
        instance.save()
    print(sender, instance)
    print("student object created")

class CustomerFather(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    age=models.IntegerField(null=True,blank=True)
    father_name = models.ForeignKey(CustomerFather, on_delete=models.CASCADE, null=True, blank=True)


