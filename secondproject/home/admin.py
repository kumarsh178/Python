from django.contrib import admin
from .models import Student,Customer

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","phone","city")
    search_fields = ("name",)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Student)