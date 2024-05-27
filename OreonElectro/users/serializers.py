from .models import Customer
from django.contrib.auth.forms import PasswordResetForm
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password', 'shipping_address', 'billing_address', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                shipping_address=validated_data['shipping_address'],
                billing_address=validated_data.get('billing_address', ''),
                phone_number=validated_data['phone_number'],
        )
        return user


class PasswordResetSerializer(serializers.ModelSerializer):
    """
    """
    email = serializers.EmailField()

    def validate_email(self, value):
        """
        Check that the user with the provided email exists.
        """
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user is registered with this email address")
        return value

    def save(self):
        """
        Overriding the save method to handle form save functionality
        """
        email = self.validated_data['email']
        form = PasswordResetForm({'email': email})
        if form.is_valid():
            form.save(
                    use_https=True,
                    from_email=None,
                    email_template_name='registration/password_reset_email.html',
                    request=self.context.get('request')
            )
