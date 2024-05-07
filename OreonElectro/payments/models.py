from django.db import models
from django.conf import settings
from orders.models import Order


class PaymentStatus(models.TextChoices):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    CANCELED = 'Canceled'


class PaymentGateway(models.TextChoices):
    PAYPAL = 'PayPal'
    MPESA = 'M-Pesa'
    STRIPE = 'Stripe'
    CREDIT_CARD = 'Credit Card'


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    gateway = models.CharField(max_length=50, choices=PaymentGateway.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment {self.id} for Order {self.order.id}'
