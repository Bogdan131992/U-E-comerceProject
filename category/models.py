from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=40, unique=True)
    category_url = models.CharField(max_length=150, unique=True)
    category_image = models.ImageField(upload_to= 'photos/categories', blank=True)
    about = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.category_name
