from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import SupportTicket, Conversation, Message


class SupportTicketTests(APITestCase):
    def setUp(self):
        self.ticket = SupportTicket.objects.create(
                title='Cannot Access Account',
                description='I am unable to access my account.',
                status='open'
        )
        self.url = reverse('ticket-detail', args=[self.ticket.id])

    def test_get_support_ticket(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Cannot Access Account')

    def test_create_support_ticket(self):
        data = {
                'title': 'Payment Issue',
                'description': 'There is a problem with my payment.',
                'status': 'open'
        }
        response = self.client.post(reverse('ticket-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Payment Issue')

    def test_update_support_ticket(self):
        data = {
                'title': 'Cannot Access Account',
                'description': 'I am unable to access my account properly.',
                'status': 'in_progress'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'in_progress')

    def test_delete_support_ticket(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(SupportTicket.objects.filter(id=self.ticket.id).exists())

    def test_add_conversation(self):
        url = reverse('ticket-add-conversation', args=[self.ticket.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(self.ticket.conversations.exists())


class ConversationTests(APITestCase):
    def setUp(self):
        self.ticket = SupportTicket.objects.create(
                title='Cannot Access Account',
                description='I am unable to access my account.',
                status='open'
        )
        self.conversation = Conversation.objects.create(ticket=self.ticket)
        self.url = reverse('conversation-detail', args=[self.conversation.id])

    def test_get_conversation(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ticket'], self.ticket.id)

    def test_create_conversation(self):
        data = {'ticket': self.ticket.id}
        response = self.client.post(reverse('conversation-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['ticket'], self.ticket.id)

    def test_add_message(self):
        url = reverse('conversation-add-message', args=[self.conversation.id])
        data = {'sender': 'Customer', 'content': 'I am facing this issue.'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['sender'], 'Customer')


class MessageTests(APITestCase):
    def setUp(self):
        self.ticket = SupportTicket.objects.create(
                title='Cannot Access Account',
                description='I am unable to access my account.',
                status='open'
        )
        self.conversation = Conversation.objects.create(ticket=self.ticket)
        self.message = Message.objects.create(
                conversation=self.conversation,
                sender='Customer',
                content='I am unable to access my account.'
        )
        self.url = reverse('message-detail', args=[self.message.id])

    def test_get_message(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'I am unable to access my account.')

    def test_create_message(self):
        data = {
                'conversation': self.conversation.id,
                'sender': 'Support Agent',
                'content': 'We are working on your issue.'
        }
        response = self.client.post(reverse('message-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], 'We are working on your issue.')

    def test_update_message(self):
        data = {
                'conversation': self.conversation.id,
                'sender': 'Customer',
                'content': 'I am still facing the issue.'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'I am still facing the issue.')

    def test_delete_message(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Message.objects.filter(id=self.message.id).exists())
