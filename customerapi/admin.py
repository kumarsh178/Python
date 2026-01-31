from django.contrib import admin # type: ignore
from .models import Customer

# Register your models here.
admin.site.register(Customer)