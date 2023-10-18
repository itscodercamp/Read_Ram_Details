from django.db import models
from core_uuid.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True,null=True)
    category_image = models.ImageField(upload_to='Category')
    def __str__(self):
        return self.category_name

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name='Products')
    price = models.IntegerField()
    product_description = models.TextField()

    def __str__(self):
        return self.product_name

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='products_images')
    image = models.ImageField(upload_to='Product')
    def __str__(self):
        return self.category_name