from rest_framework import serializers
# from .models import Category, Project
from .models import Category, Project, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields ='__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields ='__all__'
