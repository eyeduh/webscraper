from django.contrib import admin
from .models import Category, Product
from .scraper import items

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = items.CategoryScraperItem.keys()
    list_filter = items.CategoryScraperItem(serialize=str)

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = items.ProductScraperItem.keys()
    list_filter = items.ProductScraperItem(serialize=int)

admin.site.register(Product, ProductAdmin)

