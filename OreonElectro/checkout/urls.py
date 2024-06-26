from django.urls import path
from . import views


urlpatterns = [
        path('checkout/', views.CheckoutView.as_view(), name='checkout'),
        path('order_confirmation/', views.OrderConfirmationView.as_view(), name='order_confirmation'),
        path('', views.OrderListView.as_view(), name='order-list'),
        path('latest/', views.OrderDetailView.as_view(), name='latest-order'),
]
