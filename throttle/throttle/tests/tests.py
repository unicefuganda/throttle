# throttle/tests.py

from throttle.models import KannelMessage
from django.test import TestCase, SimpleTestCase
from django.test.client import Client


class KannelMessageTests(SimpleTestCase):
    """ KannelMessage Model tests """

    def test_str(self):
        kannel_message = KannelMessage(
            backend='fake',
            sender='256712123456',
            message='fake message'
        )

        self.assertEqual(
            str(kannel_message),
            'Message from 256712123456 on fake'
        )


class KannelMessageListViewTests(TestCase):
    """ KannelMessage list view tests. """

    def test_messages_in_the_context(self):
        client = Client()
        response = client.get('/')

        self.assertEquals(list(response.context['object_list']), [])
        KannelMessage.objects.create(
            backend='fake',
            sender='256712123456',
            message='fake message for listview'
        )
        response = client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)


class ReceiveTestCase(SimpleTestCase):
    payload = {
        'backend': 'yo',
        'sender': '256712345678',
        'message': 'Testing proper receive call'
    }

    def setUp(self):
        self.client = Client()
        pass

    def test_receive_returns_201(self):
        response = self.client.get('/receive/', self.payload)
        self.assertEqual(response.status_code, 201)

    def test_message_stored(self):
        self.client.get('/receive/', self.payload)
        messages = KannelMessage.objects.all()
        self.assertEqual(messages.count(), 1)
