from rest_framework import generics
from .models import BlogPost, FAQ, StaticPage
from .serializers import BlogPostSerializer, FAQSerializer, StaticPageSerializer


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'


class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class StaticPageListCreateView(generics.ListCreateAPIView):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageSerializer


class StaticPageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageSerializer
    lookup_field = 'slug'
