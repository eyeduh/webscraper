from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy_djangoitem import DjangoItem
from scrapy_django_dashboard.scrapy_django_dashboard.models import Scraper

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name= 'Category Name', max_length=30)
    url = models.URLField(verbose_name= 'Category Link', max_length=100)
    category_scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(verbose_name= 'Product Name', max_length=100)
    brand = models.CharField(verbose_name= 'Product Brand', max_length=100)
    url = models.URLField(verbose_name= 'Product URL', max_length=100)
    img = models.URLField(verbose_name= 'Product Image', max_length=200)
    # product_rating = models.DecimalField(verbose_name= 'rating')
    price = models.IntegerField(verbose_name= 'Product Price', help_text='In Dollars')
    product_scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta: 
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name


class CategoryItem(DjangoItem):
    django_model = Category

class ProductItem(DjangoItem):
    django_model = Product


