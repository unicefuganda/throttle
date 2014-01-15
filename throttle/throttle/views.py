# throttle/view.py
from django.http import HttpResponse, HttpResponseNotFound
from .tasks import store_in_db


def router_receive(request):
    return HttpResponse('Received', status=200)

def receive(request):
    backend = request.GET.get('backend', 'yo')
    sender = request.GET.get('sender', None)
    message = request.GET.get('message', None)

    if sender and message:
        store_in_db(
            backend=backend,
            sender=sender,
            message=message
        )
        return HttpResponse('Created', status=201)

    return HttpResponseNotFound()
