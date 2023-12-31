from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=40, unique=True)
    category_url = models.SlugField(max_length=150, unique=True)
    category_image = models.ImageField(upload_to= 'photos/categories', blank=True)
    about = models.TextField(max_length=300, blank=True)

    class Meta:
        verbose_name= 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse ('products_by_category', args=[self.category_url])

    def __str__(self):
        return self.category_name
