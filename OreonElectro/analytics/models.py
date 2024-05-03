from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserActivity(models.Model):
    """
    Represents a user activity for analytics purposes.

    Attributes:
        user (User): The user associated with the activity.
        activity_type (str): The type of activity (e.g., 'login', 'purchase', 'view_product').
        activity_data (JSONField): Additional data related to the activity.
        timestamp (DateTime): The timestamp of when the activity occurred.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=255)
    activity_data = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} by {self.user.username}"
