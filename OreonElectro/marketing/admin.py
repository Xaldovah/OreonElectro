from django.contrib import admin
from .models import EmailCampaign, NewsletterSubscription, PromotionalActivity


@admin.register(EmailCampaign)
class EmailCampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'scheduled_date', 'created_at', 'updated_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'scheduled_date', 'created_at', 'updated_at')


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at')
    search_fields = ('email',)
    list_filter = ('is_active', 'created_at')


@admin.register(PromotionalActivity)
class PromotionalActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'created_at')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date', 'created_at')
