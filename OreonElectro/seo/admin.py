from django.contrib import admin
from .models import SEO


@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    list_display = ('page', 'meta_title', 'meta_description', 'meta_keywords', 'meta_robots')
    search_fields = ('page', 'meta_title', 'meta_description', 'meta_keywords')
