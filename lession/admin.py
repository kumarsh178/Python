from django.contrib import admin
from .models import Lession

# Register your models here.

class LessionAdmin(admin.ModelAdmin):
    list_display=("title","course","position")
admin.site.register(Lession)