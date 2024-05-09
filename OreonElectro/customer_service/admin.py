from django.contrib import admin
from .models import SupportTicket, Conversation, Message


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'created_at')


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'created_at')
    search_fields = ('ticket__title',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'sender', 'created_at')
    search_fields = ('conversation__ticket__title', 'sender')
