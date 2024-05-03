from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Customer
from .serializers import CustomerSerializer


class RegisterView(APIView):
    """
    API endpoint to register a new user.

    Args:
        request: HTTP request object containing user registration data.

    Returns:
        Response: JSON response indicating the success or failure of
        user registration
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    API endpoint to authenticate and login a user

    Args:
        request: HTTP request object containing user login credentials.

    Returns:
        Response: JSON response indicating the success or failure of user login.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    """
    API endpoint to log out a user

    Args:
        request: HTTP request object.

    Returns:
        Response: JSON response indicating the success or failure of user logout.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        auth_logout(request)
        return Response({'message': 'Logout successful!'}, status=200)


class PasswordResetView(APIView):
    """
    API endpoint to initiate a password reset for a user.

    Args:
        request: HTTP request object containing user email address.

    Returns:
        Response: JSON response indicating the success or failure of password
        reset request.
    """
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailView(APIView):
    """
    API endpoint to retrieve or update user profile details.

    Args:
        request: HTTP request object.

    Returns:
        Response: JSON response containing user profile details.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        customer = request.user.customer
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request):
        customer = request.user.customer
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
