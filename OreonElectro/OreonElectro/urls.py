from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', include('products.urls')),
    path('products/<int:pk>/', include('products.urls')),
    path('customer/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('customer/', views.customer_detail, name='customer_detail')
]
