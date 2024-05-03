from django import forms


class ReviewForm(forms.Form):
    query = forms.CharField(label='review')
