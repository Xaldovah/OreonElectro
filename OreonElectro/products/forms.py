from django import forms


class SearchForm(forms.Form):
    """
    search form class
    """
    query = forms.CharField(label='Search')
