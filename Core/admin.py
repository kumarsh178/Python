from django.contrib import admin # type: ignore
from .models import Person, Course, Grade
from django.db.models import Avg # type: ignore
from django.utils.html import format_html # type: ignore

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=("id","first_name","last_name","show_average")
    ordering=("id",)
    list_per_page=10
    @admin.display(description="Average")
    def show_average(self, obj):
        result = Grade.objects.filter(person = obj).aggregate(Avg("grade"))
        """avg = int(result["grade__avg"])
        color ='green'
        if(avg<90 and avg>60):
            color = 'yellow'
        elif avg<=60:
            color='red'
        return format_html("<span style='color:{}'>{}<span>",color,avg)"""
        return result["grade__avg"]

class CourseAdmin(admin.ModelAdmin):
    list_display=("id","name","year")
    ordering=("id",)
class GradeAdmin(admin.ModelAdmin):
    #list_display=("id","student_grade")
    ordering=("id",)
admin.site.register(Person,PersonAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Grade,GradeAdmin)