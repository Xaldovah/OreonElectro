from django.db import models


class EmailCampaign(models.Model):
    STATUS_CHOICES = [
            ('draft', 'Draft'),
            ('scheduled', 'Scheduled'),
            ('sent', 'Sent'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    scheduled_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.get_status_display()}'


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} - {"Active" if self.is_active else "Inactive"}'


class PromotionalActivity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.start_date} - {self.end_date})'
