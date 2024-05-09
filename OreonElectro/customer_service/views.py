from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SupportTicket, Conversation, Message
from .serializers import SupportTicketSerializer, ConversationSerializer, MessageSerializer


class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer

    @action(detail=True, methods=['post'], url_path='add-conversation')
    def add_conversation(self, request, pk=None):
        ticket = self.get_object()
        conversation = Conversation.objects.create(ticket=ticket)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=True, methods=['post'], url_path='add-message')
    def add_message(self, request, pk=None):
        conversation = self.get_object()
        sender = request.data.get('sender', '')
        content = request.data.get('content', '')

        if sender and content:
            message = Message.objects.create(conversation=conversation, sender=sender, content=content)
            serializer = MessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
