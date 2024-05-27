from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
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
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    """
    API endpoint to authenticate and login a user

    Args:
        request: HTTP request object containing user login credentials.

    Returns:
        Response: JSON response indicating the success or failure of user login.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'message': 'Login successful!'
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserListView(generics.ListAPIView):
    """
    API endpoint to list all users.

    Returns:
        Response: JSON response containing a list of users.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


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
        request.user.auth_token.delete()
        return Response({'message': 'Logout successful!'}, status=status.HTTP_200_OK)


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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
