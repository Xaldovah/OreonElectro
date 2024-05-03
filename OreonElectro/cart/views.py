from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from products.models import Product


class CartDetailView(APIView):
    """
    Render the cart detail page.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart.total = sum(item.subtotal for item in cart.items.all())
        cart.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCartView(APIView):
    """
    Add a product to the user's cart.

    Args:
        request: HTTP request object.
        product_id: ID of the product to add.

    Returns:
        HttpResponse: Rendered HTML response or redirection.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        user = request.user
        cart, created_at = Cart.objects.get_or_create(user=user)
        product = Product.objects.get(pk=product_id)
        quantity = request.data.get('quantity', 1)

        subtotal = product.price * quantity

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.subtotal = subtotal
        cart_item.save()

        cart.total += subtotal
        cart.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateCartView(APIView):
    """
    Update the quantity of a product in the cart.

    Args:
        request: HTTP request object.
        cart_item_id: ID of the cart item to update.

    Returns:
        HttpResponseRedirect: Redirection to the cart detail page.
    """
    permission_classes = [IsAuthenticated]

    def put(self, request, cart_item_id):
        user = request.user
        cart_item = CartItem.objects.get(pk=cart_item_id, cart__user=user)
        quantity = request.data.get('quantity')

        if quantity:
            subtotal = cart_item.product.price * quantity
            cart_item.subtotal = subtotal

            cart_item.quantity = quantity
            cart_item.save()

            cart = cart_item.cart
            cart.total += subtotal - cart_item.subtotal
            cart.save()

            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Quantity is required.'}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromCartView(APIView):
    """
    Remove a product from the cart.

    Args:
        request: HTTP request object.
        cart_item_id: ID of the cart item to remove.

    Returns:
        HttpResponseRedirect: Redirection to the cart detail page.
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request, cart_item_id):
        user = request.user
        cart_item = CartItem.objects.get(pk=cart_item_id, cart__user=user)
        cart_item.delete()
        return Response({'success': 'Cart item removed.'}, status=status.HTTP_204_NO_CONTENT)
