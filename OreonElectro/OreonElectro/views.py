from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from users.models import Customer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from users.serializers import CustomerSerializer

def home(response):
        return render(response, "OreonElectro/home.html", {})

def register(response):
    """
    View for user registration.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered template for user registration.
    """
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = UserCreationForm()
    return render(response, "OreonElectro/register.html", {"form": form})


@api_view(['POST'])
def login(response):
    """
    API endpoint to authenticate and login a user

    Args:
        request: HTTP request object containing user login credentials.

    Returns:                                
        Response: JSON response indicating the success or failure of user login.
    """
    if response.method == 'POST':
        form = AuthenticationForm(data=response.data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(response, user)
                return redirect('/customer')
        return Response({'error': 'Invalid credentials'}, status=400)


@api_view(['POST'])
def logout(response): 
    """
    API endpoint to log out a user

    Args:
        response: HTTP response object.

    Returns:
        Response: JSON response indicating the success or failure of user logout.
    """
    if response.user.is_authenticated:
        auth_logout(request)
        return render(response, "OreonElectro/home.html")
    return Response({'error': 'User is not logged in'}, status=400)


@api_view(['POST'])
def password_reset(request):
    """
    API endpoint to initiate a password reset for a user.

    Args:
        request: HTTP request object containing user email address.

    Returns:
        Response: JSON response indicating the success or failure of password
        reset request.
    """
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
        return Response({'message': 'Password reset email sent'}, status=200)
    return Response(form.errors, status=400)


@api_view(['GET', 'PUT'])
def customer_detail(request):
    """
    API endpoint to retrieve or update user profile details.

    Args:
        request: HTTP request object.

    Returns:
        Response: JSON response containing user profile details.
    """
    user = request.user
    try:
        profile = Customer.objects.get(user=user)
    except Customer.DoesNotExist:
        return Response({'error': 'Profile not found!'}, status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
