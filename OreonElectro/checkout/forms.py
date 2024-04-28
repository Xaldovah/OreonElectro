from django import forms


class CheckoutForm(forms.Form):
    """
    Checkout Form class
    """
    shipping_address = forms.CharField(max_length=100)
    billing_address = forms.CharField(max_length=100)
    payment_method = forms.ChoiceField(choices=[('mpesa', 'M-Pesa'), ('bank', 'Bank Transfer')])
