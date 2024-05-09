from django.db import models


class SEO(models.Model):
    """
    """
    page = models.CharField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=70)
    meta_description = models.CharField(max_length=160)
    meta_keywords = models.CharField(max_length=255, blank=True)
    meta_robots = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.page} - {self.meta_title}'
