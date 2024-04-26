from django.contrib import admin
from .models import *
from cart.models import Cart, CartItem


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
