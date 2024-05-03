from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product


class Order(models.Model):
    """
    Represents an order.

    Attributes:
        customer (Customer): The customer who placed the order.
        total_amount (Decimal): The total amount of the order.
        status (str): The status of the order (e.g., Pending, Shipped, Delivered).
        created_at (DateTime): The date and time when the order was created.
        updated_at (DateTime): The date and time when the order was last updated.
    """

    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    ORDER_STATUS_CHOICES = [
            (PENDING, 'Pending'),
            (SHIPPED, 'Shipped'),
            (DELIVERED, 'Delivered'),
    ]

    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"
