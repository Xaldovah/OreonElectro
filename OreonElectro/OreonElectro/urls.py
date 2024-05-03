from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),
    path('products/', include('products.urls')),
    path('customer/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('home/', views.home, name="home"),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('reviews/', include('reviews.urls'))
]
