from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .forms import SearchForm
from .serializers import ProductSerializer


class ProductListView(APIView):
    """
    Retrieve a list of all products.

    Returns:
        Render: Rendered template with a list of products.
    """
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status_400_BAD_REQUEST)


class ProductDetailView(APIView):
    """
    Retrieve details of a specific product by its primary key.

    Args:
        pk (int): The primary key of the product.

    Returns:
        Render: Rendered template with details of the product.
    """
    def get(self, request, pk):
        product = Product.objects.all()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class ProductPricingView(APIView):
    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        price = request.data.get('price')
        if price:
            product.price = price
            product.save()
        return Response({'message': 'Product pricing updated successfully'})


class ProductInventoryView(APIView):
    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        stock_quantity = request.data.get('stock_quantity')
        if stock_quantity:
            product.stock_quantity = stock_quantity
            product.save()
        return Response({'message': 'Product inventory updated successfully'})


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
