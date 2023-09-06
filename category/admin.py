from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_url': ('category_name',)}
    list_display = ('category_name', 'category_url')

admin.site.register(Category, CategoryAdmin)
