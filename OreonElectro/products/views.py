from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .forms import SearchForm
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    """
    Retrieve a list of all products.

    Returns:
        Render: Rendered template with a list of products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDetail(generics.RetrieveAPIView):
    """
    Retrieve details of a specific product by its primary key.

    Args:
        pk (int): The primary key of the product.

    Returns:
        Render: Rendered template with details of the product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class SearchView(APIView):
    """
    search view class
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query = request.GET.get('query')
        results = Product.objects.filter(name__icontains=query)
        serializer = ProductSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        form = SearchForm(request.data)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)
            serializer = ProductSerializer(results, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid form data'}, status=status.HTTP_400_BAD_REQUEST)
