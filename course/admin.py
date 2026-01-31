from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=("title","price","author","status")
    list_filter = ("author","price")

admin.site.register(Course,CourseAdmin)