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
# class Project(models.Model):
#     title = models.CharField(max_length=120)
#     image = models.CharField(max_length=120)
#     category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)

#     description = models.TextField()

#     def _str_(self):
#         return self.title