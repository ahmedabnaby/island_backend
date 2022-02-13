from unicodedata import category
from rest_framework import serializers
from .models import Category, Project


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'image')
class ProjectsSerializer(serializers.ModelSerializer):
    # categories = serializers.RelatedField(Category.title, read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'image', 'category')
