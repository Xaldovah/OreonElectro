from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for Product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ProductSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def update_price(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        price = request.data.get('price')
        if price is not None:
            product.price = price
            product.save()
            return Response({'message': 'Product pricing updated successfully'})
        return Response({'error': 'Price not provided'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def update_inventory(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        stock_quantity = request.data.get('stock_quantity')
        if stock_quantity is not None:
            product.stock_quantity = stock_quantity
            product.save()
            return Response({'message': 'Product inventory updated successfully'})
        return Response({'error': 'Stock quantity not provided'}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class SearchView(viewsets.ViewSet):
    """
    ViewSet for searching products.
    """
    permission_classes = [AllowAny]
    
    def list(self, request):
        query = request.GET.get('query', '')
        results = Product.objects.filter(name__icontains=query)
        serializer = ProductSerializer(results, many=True)
        return Response(serializer.data)
