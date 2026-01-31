from django.db import models

# Create your models here.

class EmployeeManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)
    
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_email = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    objects = EmployeeManager()
    new_manager = models.Manager

    def __str__(self):
        return self.emp_name