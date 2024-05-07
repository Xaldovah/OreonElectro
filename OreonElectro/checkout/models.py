from django.db import models
from django.conf import settings
from orders.models import Order


class PaymentMethod(models.TextChoices):
    """
    """
    CREDIT_CARD = 'Credit Card'
    MPESA = 'M-Pesa'
    PAYPAL = 'PayPal'
    STRIPE = 'Stripe'
    CASH_ON_DELIVERY = 'Cash on Delivery'


class Checkout(models.Model):
    """
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50, choices=PaymentMethod.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Checkout {self.id} by {self.user}'
