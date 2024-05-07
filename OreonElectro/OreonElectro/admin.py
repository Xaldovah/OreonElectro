from django.contrib import admin
from .models import *
from cart.models import Cart, CartItem
from payments.models import Payment
from checkout.models import Checkout
from analytics.models import UserActivity 
from localization.models import Language, Translation
from notifications.models import Notification


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payment)
admin.site.register(Checkout)
admin.site.register(UserActivity)
admin.site.register(Language)
admin.site.register(Translation)
admin.site.register(Notification)
