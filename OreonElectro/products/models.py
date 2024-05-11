from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category for products.

    Attributes:
        name (str): The name of the category.
        description (str): The description of the category.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Represents a product.

    Attributes:
        name (str): The name of the product.
        description (str): The description of the product.
        price (Decimal): The price of the product.
        stock_quantity (int): The available quantity of the product in stock.
        category (Category): The category to which the product belongs.
        created_at (DateTime): The date and time when the product was created.
        updated_at (DateTime): The date and time when the product was last updated.
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # price = MoneyField(max_digits=7, decimal_places=2, default_currency='KES')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
