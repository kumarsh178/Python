from django.db import models

class Father(models.Model):
    name=models.CharField(max_length=100)
    desChoice=(("mg","Manager"),("fr","Farmer"),("sfr","Software Engineer"))
    designation=models.CharField(max_length=50,choices=desChoice)
    #this will decide which will be shon as lebel
    def __str__(self):
        return self.name
# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    genderChoices = (("male","Male"),("female","Female"))
    gender=models.CharField(max_length=30,choices=genderChoices)
    father_name=models.ForeignKey(Father,on_delete=models.CASCADE)
