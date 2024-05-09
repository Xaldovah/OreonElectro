from rest_framework import serializers
from .models import SupportTicket, Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'ticket', 'created_at', 'messages']


class SupportTicketSerializer(serializers.ModelSerializer):
    conversations = ConversationSerializer(many=True, read_only=True)

    class Meta:
        model = SupportTicket
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at', 'conversations']
