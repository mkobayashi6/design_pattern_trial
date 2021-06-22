from django.contrib import admin

# for Django tutorial
from .models import Category, SubCategory

admin.site.register(Category)
admin.site.register(SubCategory)