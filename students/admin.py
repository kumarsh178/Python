from django.contrib import admin
from .models import Father, Students

# Register your models here.
class FatherAdmin(admin.ModelAdmin):
    list_display=("id","name","designation")
class StudentsAdmin(admin.ModelAdmin):
    list_display=("id","name","email","gender","father_name")
admin.site.register(Father,FatherAdmin)
admin.site.register(Students, StudentsAdmin)