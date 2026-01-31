from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display=("id","name","email","city","phone")
    list_per_page=10
admin.site.register(Customer,CustomerAdmin)

# Register your models here.
