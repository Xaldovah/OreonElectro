from django.urls import path
from . import views


urlpatterns = [
        path('orders/history/', views.OrderHistoryView.as_view(), name='order_history'),
        path('orders/create/', views.CreateOrderView.as_view(), name='create_order'),
        path('orders/<pk>/update/', views.UpdateOrderView.as_view(), name='update_order'),
        path('orders/<pk>/delete/', views.DeleteOrderView.as_view(), name='delete_order'),
]
