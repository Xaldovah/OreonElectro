from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = User
        fields = ['user', 'shipping_address', 'billing_address', 'phone_number']


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
        if form.is_valid:
            form.save(
                    use_https=True,
                    from_email=None,
                    email_template_name='registration/password_reset_email.html',
                    request=self.context.get('request')
            )
