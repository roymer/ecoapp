from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class ProductUnits(models.TextChoicesModel):
    UNITS = 'u', 'Unidades',
    KG = 'kg', 'Kilogramos',

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unity = models.CharField(
        max_length=2,
        choices = ProductUnits.choices,
        default = ProductUnits.UNITS 
    )
    disponible = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)