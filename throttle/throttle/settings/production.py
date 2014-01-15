from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'throttle',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

ROUTER_URL = 'http://ureport.unicefuganda.org/router/receive/'
ROUTER_PASSWORD = 'k1pr0t1ch'
CELERYBEAT_SCHEDULE = {
    'add-every-second': {
        'task': 'throttle.tasks.send_to_router',
        'schedule': timedelta(seconds=10),
        'args': None
    },
}
