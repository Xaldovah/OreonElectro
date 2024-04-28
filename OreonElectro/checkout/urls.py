from django.urls import path
from . import views


urlpatterns = [
        path('', views.checkout, name='checkout'),
        path('confirmation/', views.order_confirmation, name='order_confirmation'),
]
