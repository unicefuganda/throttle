from __future__ import absolute_import

import requests
from .models import KannelMessage
from celery import task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.exceptions import DoesNotExist
from django.db import transaction

logger = get_task_logger(__name__)
url = settings.ROUTER_URL
password = settings.ROUTER_PASSWORD
s = requests.session()


@task
def store_in_db(backend, sender, message):
    message = KannelMessage.objects.create(
        backend=backend,
        sender=sender,
        message=message,
        handled=False
    )
    return message.id


@task
def mark_handled(backend, sender, message):
    with transaction.commit_on_success():
        try:
            m = KannelMessage.objects.filter(
                backend=backend,
                sender=sender,
                message=message
            ).select_for_update().earliest()
            m.handled = 1
            m.save()
        except DoesNotExist:
            pass


@task
def send_directly_to_router(backend, sender, message):
    payload = {
        'backend': backend,
        'password': password,
        'sender': sender,
        'message': message,
        'throttled': 1,
    }
    logger.info("Calling url: %s with payload: %s" % (url, payload))
    response = s.get(url, params=payload)
    logger.debug(response.text)
    mark_handled.delay(backend, sender, message)


@transaction.atomic
@task(bind=True)
def send_to_router(unused):
    with transaction.commit_on_success():
        m = KannelMessage.objects.select_for_update().earliest()
        send_directly_to_router(m.backend, m.sender, m.message)
        m.delete()
