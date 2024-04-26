from django import forms


class AddToCartForm(forms.Form):
    """
    Form for adding products to the cart.

    Attributes:
        quantity (IntegerField): The quantity of the product to add to the
        cart.
    """
    quantity = forms.IntegerField(min_value=1, label='Quantity')
