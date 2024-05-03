from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    """
    Represents a notification for a user.

    Attributes:
        user (User): The user to whom the notification is sent.
        title (str): The title of the notification.
        message (str): The content of the notification.
        is_read (bool): Whether the notification has been read or not.
        created_at (DateTime): The date and time when the notification was created.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} for {self.user.username}"
