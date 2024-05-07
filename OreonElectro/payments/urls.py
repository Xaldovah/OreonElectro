from django.urls import path
from . import views


urlpatterns = [
        path('', views.PaymentView.as_view(), name='payment'),
        path('<int:pk>/', views.PaymentStatusView.as_view(), name='payment-status'),
        path('user-payments/', views.UserPaymentsView.as_view(), name='user-payments'),
]
