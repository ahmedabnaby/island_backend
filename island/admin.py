from django.contrib import admin

# Register your models here.
from .models import Category, Project

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

# Register your models here.

admin.site.register(Category, CategoryAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category')

# Register your models here.

admin.site.register(Project, ProjectAdmin)