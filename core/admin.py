from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=("id","title","author","published_year")
    list_filter=("published_year","author")
    list_per_page=10
admin.site.register(Book,BookAdmin)
