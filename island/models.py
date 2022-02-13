from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=120)
    image = models.CharField(max_length=120)
    # image = models.ImageField(null=True, blank=True)

    description = models.TextField()

    def _str_(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=120)
    image = models.CharField(max_length=120)
    # image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)

    description = models.TextField()

    def _str_(self):
        return self.title