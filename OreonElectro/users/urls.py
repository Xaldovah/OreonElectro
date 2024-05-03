from django.urls import path
from . import views


urlpatterns = [
        path('register/', views.RegisterView.as_view(), name='register'),
        path('login/', views.LoginView.as_view(), name='login'),
        path('logout/', views.LogoutView.as_view(), name='logout'),
        path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
        path('customer/', views.CustomerDetailView.as_view(), name='customer_detail'),
]
