from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


def product_list(request):
    """
    Retrieve a list of all products.

    Returns:
        JsonResponse: JSON response containing a list of products.
    """
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
    return JsonResponse(data, safe=False)


def product_detail(request, pk):
    """
    Retrieve details of a specific product ID.

    Args:
        pk (INT): The ID of the product.

    Returns:
        JsonResponse: JSON response containing details of the product.
    """
    try:
        product = Product.objects.get(pk=pk)
        data = {'id': product.id, 'name': product.name, 'price': product.price}
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
