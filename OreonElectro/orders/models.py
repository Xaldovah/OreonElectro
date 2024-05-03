from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.db.models import EmailField

User = get_user_model()


class Order(models.Model):
    """
    Represents an order.

    Attributes:
        customer (User): The customer who placed the order.
        shipping_address (CharField): The shipping address for the order.
        billing_address (CharField): The billing address for the order.
        phone_number (CharField): The phone number associated with the order.
        email (EmailField): The email address associated with the order.
        payment_method (CharField): The payment method used for the order.
        payment_status (CharField): The status of the payment (pending, completed, failed).
        fulfillment_status (CharField): The status of order fulfillment (pending, processing, shipped, delivered, cancelled).
        tracking_number (CharField): The tracking number for shipped orders.
        total_amount (DecimalField): The total amount of the order.
        status (CharField): The status of the order (pending, shipped, delivered).
        created_at (DateTimeField): The date and time when the order was created.
        updated_at (DateTimeField): The date and time when the order was last updated.

    Methods:
        update_total_amount: Updates the total amount of the order based on its items.
        
    Strings:
        __str__: Returns a string representation of the order.
    """
    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'
    ORDER_STATUS_CHOICES = [
            (PENDING, 'Pending'),
            (SHIPPED, 'Shipped'),
            (DELIVERED, 'Delivered'),
            (CANCELLED, 'Cancelled'),
    ]
    shipping_address = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending')

    fulfillment_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default=PENDING)
    tracking_number = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_total_amount(self):
        """
        Update the total amount of the order based on its items.
        """
        self.total_amount = sum(item.subtotal for item in self.order_items.all())
        self.save()

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"


class OrderItem(models.Model):
    """
    Represents an item within an order.

    Attributes:
        order (Order): The order to which the item belongs.
        product (Product): The product associated with the item.
        quantity (int): The quantity of the product in the order.
        subtotal (Decimal): The subtotal for the item.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        """
        Override the save method to update the order's total amount
        """
        self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total_amount()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"
