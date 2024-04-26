from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('products', include('products.urls')),
    path('products/<int:pk>/', include('products.urls')),
    path('customer/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('home/', views.home, name="home"),
    path('register/', csrf_exempt(views.register), name='register'),
    path('login/', csrf_exempt(views.login), name='login'),
    path('logout/', views.logout, name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('customer/', views.customer_detail, name='customer_detail'),
    path('cart/', include('cart.urls'))
]
