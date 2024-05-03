from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product


class Cart(models.Model):
    """
    Represents a user's shopping cart.

    Attributes:
        user (User): The user who owns the cart.
        created_at (DateTime): The date and time when the cart was created.
        updated_at (DateTime): The date and time when the cart was last updated.
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    """
    Represents an item within a shopping cart.

    Attributes:
        cart (Cart): The cart to which the item belongs.
        product (Product): The product associated with the item.
        quantity (int): The quantity of the product in the cart.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"
