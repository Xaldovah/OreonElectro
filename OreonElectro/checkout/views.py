from django.shortcuts import render, redirect
from .forms import CheckoutForm
from orders.models import Order


def checkout(request):
    """
    checkout method
    """
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            shipping_address = form.cleaned_data['shipping_address']
            billing_address = form.cleaned_data['billing_address']
            payment_method = form.cleaned_data['payment_method']

            order = Order.objects.create(
                    user=request.user,
                    shipping_address=shipping_address,
                    billing_address=billing_address,
                    payment_method=payment_method,
                    status='Pending'
            )

            for cart_item in request.user.cart.items.all():
                OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity, subtotal=cart_item.subtotal)

            request.user.cart.clear()

            return redirect('order_confirmation')

    else:
        form = CheckoutForm()
    return render(request, 'checkout/checkout_form.html', {'form': form})


def order_confirmation(request):
    """
    order confirmation
    """
    order = Order.objects.filter(user=request.user).latest('created_at')
    return render(request, 'checkout/order_confirmation.html', {'order': order})
