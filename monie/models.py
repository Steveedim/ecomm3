from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = [ 'name']
    def __str__(self):
        return self.name




class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length= 100, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    description = models.TextField()
    is_sold = models.BooleanField(default=False, null=True)
    stock = models.IntegerField(null=True)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity  = models.IntegerField(null=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return self.name