from django.urls import path
from . import views


urlpatterns = [
        path('<int:product_id>/add_review/', views.add_review, name='add_review'),
        path('<int:product_id>/view_reviews/', views.view_reviews, name='view_reviews'),
]
