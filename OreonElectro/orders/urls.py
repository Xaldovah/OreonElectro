from django.urls import path
from . import views


urlpatterns = [
        path('history/', views.OrderHistoryView.as_view(), name='order_history'),
        path('create/', views.CreateOrderView.as_view(), name='create_order'),
        path('<int:pk>/update/', views.UpdateOrderView.as_view(), name='update_order'),
        path('<int:pk>/fulfill/', views.FulfillOrderView.as_view(), name='fulfill_order'),
        path('<int:pk>/status/', views.UpdateOrderStatusView.as_view(), name='update_status'),
        path('<int:pk>/delete/', views.DeleteOrderView.as_view(), name='delete_order'),
]
