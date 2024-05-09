from django.urls import path
from .views import (
        BlogPostListCreateView, BlogPostRetrieveUpdateDestroyView,
        FAQListCreateView, FAQRetrieveUpdateDestroyView,
        StaticPageListCreateView, StaticPageRetrieveUpdateDestroyView
)


urlpatterns = [
        path('blog-posts/', BlogPostListCreateView.as_view(), name='blog-post-list-create'),
        path('blog-posts/<slug:slug>/', BlogPostRetrieveUpdateDestroyView.as_view(), name='blog-post-retrieve-update-destroy'),
        path('faqs/', FAQListCreateView.as_view(), name='faq-list-create'),
        path('faqs/<int:pk>/', FAQRetrieveUpdateDestroyView.as_view(), name='faq-retrieve-update-destroy'),
        path('static-pages/', StaticPageListCreateView.as_view(), name='static-page-list-create'),
        path('static-pages/<slug:slug>/', StaticPageRetrieveUpdateDestroyView.as_view(), name='static-page-retrieve-update-destroy'),
]
