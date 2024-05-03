from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from products.models import Product


class AddReviewView(APIView):
    """
    add reviews to the product
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        user = request.user
        product = Product.objects.get(pk=product_id)
        data = request.data.copy()
        data['product'] = product.id
        data['user'] = user.id

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewReviewsView(APIView):
    """
    view reviews
    """
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        reviews = Review.objects.filter(product=product)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
