from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Customer
from .serializers import CustomerSerializer


@api_view(['POST'])
def register(request):
    """
    API endpoint to register a new user.

    Args:
        request: HTTP request object containing user registration data.

    Returns:
        Response: JSON response indicating the success or failure of
        user registration
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return Response({'message': 'User created successfully!'}, status=201)
        return Response(form.errors, status=400)


@api_view(['POST'])
def login(request):
    """
    API endpoint to authenticate and login a user

    Args:
        request: HTTP request object containing user login credentials.

    Returns:
        Response: JSON response indicating the success or failure of user login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return Response({'message': 'Login successful!'}, status=200)
        return Response({'error': 'Invalid credentials'}, status=400)


@api_view(['POST'])
def logout(request):
    """
    API endpoint to log out a user

    Args:
        request: HTTP request object.

    Returns:
        Response: JSON response indicating the success or failure of user logout.
    """
    if request.user.is_authenticated:
        auth_logout(request)
        return Response({'message': 'Logout successful!'}, status=200)
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
@permission_classes([IsAuthenticated])
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
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found!'}, status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=404)
