from .base import *

# Use sqlite3 to speed up the tests, we omit the TEST_NAME so that tests use a
# memory resident database (see:
# https://docs.djangoproject.com/en/1.6/ref/settings/#test-name)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

STORE_KANNEL_MESSAGES_IN_DB = True
CELERY_ALWAYS_EAGER = True
