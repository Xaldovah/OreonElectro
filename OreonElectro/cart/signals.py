from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CartItem


@receiver(post_save, sender=CartItem)
def update_cart_total(sender, instance, **kwargs):
    cart = instance.cart
    cart.total = sum(item.subtotal for item in cart.items.all())
    cart.save()


@receiver(post_delete, sender=CartItem)
def update_cart_total_on_delete(sender, instance, **kwargs):
    cart = instance.cart
    cart.total = sum(item.subtotal for item in cart.items.all())
    cart.save()


post_save.connect(update_cart_total, sender=CartItem)
post_delete.connect(update_cart_total_on_delete, sender=CartItem)
