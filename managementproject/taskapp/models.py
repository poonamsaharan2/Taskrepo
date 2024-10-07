
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
class Supplier(models.Model):
    name = models.CharField(max_length=60)
    contact_info = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')  # Added priority field

    def __str__(self):
        return self.name




