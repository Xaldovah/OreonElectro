from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    Represents a customer.

    Attributes:
        user (User): The user associated with the customer.
        shipping_address (str): The shipping address of the customer.
        billing_address (str): The billing address of the customer.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    billing_address = models.TextField()

    def __str__(self):
        return self.user.username
