
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer, ProjectSerializer, NewsSerializer

from .models import Category,Project,News
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



@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/newss/',
		'Detail View':'/news-detail/<str:pk>/',
		'Create':'/news-create/',
		'Update':'/news-update/<str:pk>/',
		'Delete':'/news-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def newsList(request):
	newss = News.objects.all().order_by('-id')
	serializer = NewsSerializer(newss, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def newsDetail(request, pk):
	newss = News.objects.get(id=pk)
	serializer = NewsSerializer(newss, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def newsCreate(request):
	serializer = NewsSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def newsUpdate(request, pk):
	news = News.objects.get(id=pk)
	serializer = NewsSerializer(instance=news, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def newsDelete(request, pk):
	news = News.objects.get(id=pk)
	news.delete()

	return Response('Item succsesfully delete!')













