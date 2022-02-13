from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, ProjectsSerializer
from .models import Category, Project
from rest_framework.decorators import api_view

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @api_view(['POST'])
    def uploadImage(request):
        data = request.data

        obj_id = data['obj_id']
        obj= Category.objects.get(id=obj_id)

        obj.image = request.FILES.get('image')
        obj.save()

        return response('Image was uploaded')

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Project.objects.all()

    @api_view(['POST'])
    def uploadImage(request):
        data = request.data

        obj_id = data['obj_id']
        obj= Project.objects.get(id=obj_id)

        obj.image = request.FILES.get('image')
        obj.save()

        return response('Image was uploaded')
