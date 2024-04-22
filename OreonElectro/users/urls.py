from django.urls import path
from . import views


urlpatterns = [
        path('register/', views.register, name='register'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
        path('password-reset/', views.password_reset, name='password_reset'),
        path('customer/', views.customer_detail, name='customer_detail'),
]
