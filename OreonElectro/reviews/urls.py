from django.urls import path
from . import views


urlpatterns = [
        path('<int:product_id>/add_review/', views.AddReviewView.as_view(), name='add_review'),
        path('<int:product_id>/view_reviews/', views.ViewReviewsView.as_view(), name='view_reviews'),
]
