from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
        openapi.Info(
            title="OreonElectro API",
            default_version='v1',
            description="API documentation for the OreonElectro project",                                 terms_of_service="https://www.google.com/policies/terms/",                                    contact=openapi.Contact(email="support@oreonelectro.com"),                                    license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/seo/', include('seo.urls')),
    path('api/content/', include('content.urls')),
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
    path('api/promotions/', include('promotions.urls')),
    path('api/shipping/', include('shipping.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/reporting/', include('reporting.urls')),
    path('api/customer_service/', include('customer_service.urls')),
    path('api/marketing/', include('marketing.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
