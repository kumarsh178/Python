from django.db import models

# Create your models here.
class Store(models.Model):
    bmp_id = models.CharField(null=True, max_length=100)
    store_name = models.CharField(max_length=100)