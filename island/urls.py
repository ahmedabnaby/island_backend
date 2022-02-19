from django.urls import path
from . import views

urlpatterns = [

	path('', views.apiOverview, name="api-overview"),
    path('categories/', views.categoryList, name="categories"),
	path('category-detail/<str:pk>/', views.categoryDetail, name="category-detail"),
	path('category-create/', views.categoryCreate, name="category-create"),

	path('category-update/<str:pk>/', views.categoryUpdate, name="category-update"),
	path('category-delete/<str:pk>/', views.categoryDelete, name="category-delete"),

	path('projects/', views.projectList, name="projects"),
	path('project-detail/<str:pk>/', views.projectDetail, name="project-detail"),
	path('project-create/', views.projectCreate, name="project-create"),

	path('project-update/<str:pk>/', views.projectUpdate, name="project-update"),
	path('project-delete/<str:pk>/', views.projectDelete, name="project-delete"),
]
