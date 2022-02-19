
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer, ProjectSerializer

from .models import Category,Project
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/category-list/',
		'Detail View':'/category-detail/<str:pk>/',
		'Create':'/category-create/',
		'Update':'/category-update/<str:pk>/',
		'Delete':'/category-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def categoryList(request):
	categorys = Category.objects.all().order_by('-id')
	serializer = CategorySerializer(categorys, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def categoryDetail(request, pk):
	categorys = Category.objects.get(id=pk)
	serializer = CategorySerializer(categorys, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def categoryCreate(request):
	serializer = CategorySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def categoryUpdate(request, pk):
	category = Category.objects.get(id=pk)
	serializer = CategorySerializer(instance=category, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def categoryDelete(request, pk):
	category = Category.objects.get(id=pk)
	category.delete()

	return Response('Item succsesfully delete!')


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/projects/',
		'Detail View':'/project-detail/<str:pk>/',
		'Create':'/project-create/',
		'Update':'/project-update/<str:pk>/',
		'Delete':'/project-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def projectList(request):
	projects = Project.objects.all().order_by('-id')
	serializer = ProjectSerializer(projects, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def projectDetail(request, pk):
	projects = Project.objects.get(id=pk)
	serializer = ProjectSerializer(projects, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def projectCreate(request):
	serializer = ProjectSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def projectUpdate(request, pk):
	project = Project.objects.get(id=pk)
	serializer = ProjectSerializer(instance=project, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def projectDelete(request, pk):
	project = Project.objects.get(id=pk)
	project.delete()

	return Response('Item succsesfully delete!')













