from django.contrib import admin # type: ignore
from .models import Products, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'slug', 'category', 'created_at')
    prepopulated_fields = ({"slug": ('name', )})

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = ({"slug": ('name', ) })



admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)