from django.contrib import admin
from .models import Courses

# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
    list_display = ("title","courses","video_url")
    list_filter=("courses",)
    #autocomplete_fields=("courses",)

#admin.site.register(Courses,CoursesAdmin)