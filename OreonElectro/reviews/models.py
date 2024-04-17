from django.db import models
from users.models import Customer
from products.models import Product


class Review(models.Model):
    """
    Represents a product review.

    Attributes:
        product (Product): The product being reviewed.
        customer (Customer): The customer who wrote the review.
        rating (int): The rating given to the product (from 1 to 5).
        comment (str): The comment or review text.
        created_at (DateTime): The date and time when the review was created.
        updated_at (DateTime): The date and time when the review was last updated.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
