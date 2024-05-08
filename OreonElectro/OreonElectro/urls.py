from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/products/', include('products.urls')),
    path('api/customer/', include('users.urls')),
    path('api/orders/', include('orders.urls')),
    path('home/', views.home, name="home"),
    path('api/cart/', include('cart.urls')),
    path('api/checkout/', include('checkout.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/localization/', include('localization.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/promotions/', include('promotions.urls'))
]
