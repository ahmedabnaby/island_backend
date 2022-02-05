from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
                serializer.save(
                category=Category.objects.get(code=request.data.get('categories')),
                image=request.data.get('image')
            )
        return Response(data=serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
