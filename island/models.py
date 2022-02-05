from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=120)
    # image = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to='uploads/categories/',
        max_length=254, blank=True, null=True
    )
    description = models.TextField()

    def _str_(self):
        return self.title