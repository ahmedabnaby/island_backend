from django.contrib import admin

# Register your models here.
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

# Register your models here.

admin.site.register(Category, CategoryAdmin)