from django.contrib import admin
from .models import Company, Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=("company_id","name","location","about","type","active")
    #ASC orde
    ordering=("-company_id",)
    #DESC ORDER
    ordering=("company_id",)
admin.site.register(Company,CompanyAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=("id","name","email","address","phone","about","company")
    list_per_page=15

admin.site.register(Employee, EmployeeAdmin)