from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import SearchForm


def product_list(request):
    """
    Retrieve a list of all products.

    Returns:
        Render: Rendered template with a list of products.
    """
    products = Product.objects.all()
    return render(request, "products/product_detail.html", {"products": products})


def product_detail(request, pk):
    """
    Retrieve details of a specific product by its primary key.

    Args:
        pk (int): The primary key of the product.

    Returns:
        Render: Rendered template with details of the product.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})


def search(request):
    """
    Search a product
    """
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)
            return render(request, 'products/search_results.html', {'results': results})
    
    else:
        form = SearchForm()
    return render(request, 'products/search_form.html', {'form': form})
