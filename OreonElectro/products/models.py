from django.db import models


class Category(models.Model):
    """
    Represents a category for products.

    Attributes:
        name (str): The name of the category.
        description (str): The description of the category.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

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
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
