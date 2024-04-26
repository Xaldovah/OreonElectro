from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from .forms import AddToCartForm


@login_required
def cart_detail(request):
    """
    Render the cart detail page.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response.
    """
    cart = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/detail.html', {'cart': cart})


@login_required
def add_to_cart(request, product_id):
    """
    Add a product to the user's cart.

    Args:
        request: HTTP request object.
        product_id: ID of the product to add.

    Returns:
        HttpResponse: Rendered HTML response or redirection.
    """
    cart = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item = CartItem.objects.create(cart=cart, product_id=product_id, quantity=quantity)
            messages.success(request, f'Product added to cart.')
            return redirect('cart_detail')
    else:
        form = AddToCartForm()
    return render(request, 'cart/add_to_cart.html', {'form': form})


@login_required
def update_cart(request, cart_item_id):
    """
    Update the quantity of a product in the cart.

    Args:
        request: HTTP request object.
        cart_item_id: ID of the cart item to update.

    Returns:
        HttpResponseRedirect: Redirection to the cart detail page.
    """
    if request.method == 'POST':
        cart_item = CartItem.objects.get(pk=cart_item_id)
        quantity = request.POST.get('quantity')
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(redirect, f'Cart updated.')
    return redirect('cart_detail')


@login_required
def remove_from_cart(request, cart_item_id):
    """
    Remove a product from the cart.

    Args:
        request: HTTP request object.
        cart_item_id: ID of the cart item to remove.

    Returns:
        HttpResponseRedirect: Redirection to the cart detail page.
    """
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    messages.success(request, f'Product removed from cart.')
    return redirect('cart_detail')
