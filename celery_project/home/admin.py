from django.contrib import admin
from .models import Customer

# Register your models here.
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","phone","city")
    search_fields = ("name",)

admin.site.register(Customer,CustomerAdmin)