from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.TextField()
    img=models.ImageField(upload_to="images")
    des=models.TextField()
    short_des=models.TextField()
    price=models.FloatField()
    sku=models.CharField(max_length=100)
    created_date=models.DateField()
    ptypeChoices = [
        ("simple","Simple"),
        ("configurable","Configurable"),
        ("group","Groupd"),
        ("virtual","Virtual"),
        ("bundle","Bundle"),
        ("downloadable","Downloadable")
        ]
    product_type=models.CharField(choices=ptypeChoices, max_length=100)
    sell_price=models.FloatField()
    qty=models.IntegerField(default=1000)
    statusChoice = [("enable","Enable"),("disable","Disable")]
    status=models.CharField(choices=statusChoice, max_length=100)
    def capital_sku(self):
        return self.sku.upper()
    def __str__(self):
        return self.name
    class Meta: 
        db_table = 'coreapp_products'
        # Add verbose name 
        verbose_name = 'Manage Products'