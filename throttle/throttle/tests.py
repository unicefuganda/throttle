# throttle/tests.py

from django.test import SimpleTestCase
from django.test.client import Client

from .models import KannelMessage


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
