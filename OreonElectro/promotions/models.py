from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Discount(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text=_("Percentage discount, e.g., 10.00 for 10%"))
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.percentage}%'


class Coupon(models.Model):
    """
    """
    code = models.CharField(max_length=50, unique=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='coupons')
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_valid(self):
        now = timezone.now()
        return self.active and (self.valid_from <= now <= self.valid_to)

    def save(self, *args, **kwargs):
        if not self.is_valid():
            self.active = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code


class Promotion(models.Model):
    """
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='promotions')
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_active(self):
        now = timezone.now()
        return self.active and (self.valid_from <= now <= self.valid_to)

    def save(self, *args, **kwargs):
        if not self.is_valid():
            self.active = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
