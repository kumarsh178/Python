from django.contrib import admin # type: ignore
from .models import Lession
from .models import Course

# Register your models here.

class LessonInline(admin.TabularInline):
    model= Lession

class CourseAdmin(admin.ModelAdmin):
    list_display=("title","price","author","status")
    list_filter = ("author","price")
    search_fields=("title","price")
    list_per_page = 3
    #ordering=("title",)
    readonly_fields = ("title","price")
    inlines=(LessonInline,)
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("title",)
        else:
            return ("-price",)

class LessionAdmin(admin.ModelAdmin):
    list_display=("title","course","position")
    list_filter=("course",)
    #autocomplete_fields=("course",)
    #raw_id_fields = ("course",)

admin.site.register(Course,CourseAdmin)
admin.site.register(Lession,LessionAdmin)

