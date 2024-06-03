from django.urls import path
from .views import ProductViewSet, SearchView, product_list, product_detail

urlpatterns = [
        path('products-list/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
        path('products-detail/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),
        path('<int:pk>/update_price/', ProductViewSet.as_view({'put': 'update_price'}), name='product-update-price'),
        path('<int:pk>/update_inventory/', ProductViewSet.as_view({'put': 'update_inventory'}), name='product-update-inventory'),
        path('search/', SearchView.as_view({'get': 'list'}), name='product-search'),
        path('', product_list, name='products-list'),
        path('<int:pk>/', product_detail, name='product-detail'),
]
