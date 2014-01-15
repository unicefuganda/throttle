# throttle/tests.py

from throttle.models import KannelMessage
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class KannelMessageListIntegrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(KannelMessageListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(KannelMessageListIntegrationTests, cls).tearDownClass()

    def test_message_listed(self):
        # create a test message
        KannelMessage.objects.create(
            backend='fake',
            sender='256712123456',
            message='fake message for listview integration'
        )
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.message')[0].text,
            'Message from 256712123456 on fake'
        )

    def test_add_message_linked(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assert_(
            self.selenium.find_element_by_link_text('add message')
        )

    def test_add_message(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_link_text('add message').click()

        self.selenium.find_element_by_id('id_backend').send_keys('fake')
        self.selenium.find_element_by_id(
            'id_sender'
        ).send_keys('2567121324354')
        self.selenium.find_element_by_id('id_message').send_keys('message two')

        self.selenium.find_element_by_id('save_message').click()
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.message')[-1].text,
            'Message from 2567121324354 on fake'
        )
