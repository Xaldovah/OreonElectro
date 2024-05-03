from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Customer(models.Model):
    """
    Represents a customer.

    Attributes:
        user (User): The user associated with the customer.
        shipping_address (str): The shipping address of the customer.
        billing_address (str): The billing address of the customer.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    shipping_address = models.TextField()
    billing_address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    payment_method_choices = [
            ('bank', 'Bank Transfer'),
            ('mpesa', 'M-Pesa'),
            ('paypal', 'PayPal'),
            ('stripe', 'Stripe'),
    ]
    payment_method = models.CharField(max_length=10, choices=payment_method_choices, db_index=True)

    def __str__(self):
        return self.user.username
