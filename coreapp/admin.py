from django.contrib import admin
from .models import Products;

admin.site.site_header="CUSTOM ADMIN PROJECT"
admin.site.site_title="CUSTOM ADMIN PROJECT"
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    #to display column
    list_display = ("id","name","sku","price","product_type","created_date","status","capital_sku")
    #exclude = ("img","status")
    list_display_links=("name","sku")
    list_editable=("price","status")
    list_filter=("status","price")
    search_fields=("name__startswith","sku","price__gte")


admin.site.register(Products, ProductsAdmin)
