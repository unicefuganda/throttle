from __future__ import absolute_import

import requests
from .models import KannelMessage
from celery import task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

logger = get_task_logger(__name__)
url = settings.ROUTER_URL
s = requests.session()


@task
def store_in_db(backend, sender, message):
    message = KannelMessage.objects.create(
        backend=backend,
        sender=sender,
        message=message
    )
    return message.id


@transaction.atomic
@task(bind=True)
def send_to_router(unused):
    url = settings.ROUTER_URL
    password = settings.ROUTER_PASSWORD
    with transaction.commit_on_success():
        m = KannelMessage.objects.select_for_update().earliest()
        try:
            payload = {
                'backend': m.backend,
                'password': password,
                'sender': m.sender,
                'message': m.message,
                'throttled': 1,
            }
            logger.info("Calling url: %s with payload: %s" % (url, payload))
            r = requests.get(url, params=payload)
            logger.debug(r.text)
            m.delete()
        except ObjectDoesNotExist:
            pass
