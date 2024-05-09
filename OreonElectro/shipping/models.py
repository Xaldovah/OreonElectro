from django.db import models


class ShippingProvider(models.Model):
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class ShippingOption(models.Model):
    name = models.CharField(max_length=100, unique=True)
    provider = models.ForeignKey(ShippingProvider, on_delete=models.CASCADE, related_name='options')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.provider.name})'


class ShippingRate(models.Model):
    option = models.ForeignKey(ShippingOption, on_delete=models.CASCADE, related_name='rates')
    weight_min = models.DecimalField(max_digits=6, decimal_places=2)
    weight_max = models.DecimalField(max_digits=6, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.option.name}: {self.weight_min}kg - {self.weight_max}kg at ${self.rate}'
