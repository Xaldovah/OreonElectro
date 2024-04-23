from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

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
