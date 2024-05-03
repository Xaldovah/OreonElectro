from django.urls import path
from . import views


urlpatterns = [
        path('', views.ProductListView.as_view(), name='product_list'),
        path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
        path('<int:pk>/pricing/', views.ProductPricingView.as_view(), name='product_pricing'),
        path('<int:pk>/inventory/', views.ProductInventoryView.as_view(), name='product_inventory'),
        path('search/', views.SearchView.as_view(), name='search'),
]
