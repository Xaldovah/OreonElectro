from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review


def add_review(request, product_id):
    """
    add reviews to the product
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            
            review = Review.objects.create(product_id=product_id,
                    rating=rating,
                    comment=comment
            )
            review.user = request.user
            review.save()
            return redirect('view_reviews', product_id=product_id)

    else:
        form = ReviewForm()
    return render(request, 'reviews/add_reviews.html', {'form': form})


def view_reviews(request, product_id):
    """
    view reviews
    """
    reviews = Review.objects.filter(product_id=product_id)
    return render(request, 'reviews/view_reviews.html', {'reviews': reviews})
