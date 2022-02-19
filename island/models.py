import datetime
from django.db import models

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=200)
  image = models.CharField(max_length=200)
  description = models.TextField()
      
  def __str__(self):
    return self.title

class Project(models.Model):
  title = models.CharField(max_length=200)
  image = models.CharField(max_length=200)
  category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
  description = models.TextField()
      
  def __str__(self):
    return self.title

class News(models.Model):
  title = models.CharField(max_length=200)
  image = models.CharField(max_length=200)
  category = models.ForeignKey(Category, related_name='news', on_delete=models.CASCADE)
  description = models.TextField()
  date = models.DateTimeField(auto_now_add=True, blank=True)
      
  def __str__(self):
    return self.title

