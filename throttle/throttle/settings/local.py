from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'throttle',
        'USER': 'matlads',
        'PASSWORD': '',
        'HOST': '',
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


INSTALLED_APPS += (
    'django.contrib.admin',
    'debug_toolbar',
    'django_extensions',
)
ROUTER_URL = 'http://localhost:45524/router/receive/'

CELERY_ALWAYS_EAGER=True
