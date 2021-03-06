# throttle/view.py
from .models import KannelMessage
from .tasks import send_directly_to_router, store_in_db
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView, ListView, DetailView
from django_filters.views import FilterView


def router_receive(request):
    return HttpResponse('Received', status=200)


def receive(request):
    backend = request.GET.get('backend', 'yo')
    sender = request.GET.get('sender', None)
    message = request.GET.get('message', None)

    if sender and message:
        if settings.STORE_KANNEL_MESSAGES_IN_DB:
            store_in_db.delay(backend, sender, message)
        send_directly_to_router.delay(
            backend=backend,
            sender=sender,
            message=message
        )
        return HttpResponse('Created', status=201)

    return HttpResponseNotFound()


class KannelMessageListView(ListView):
    model = KannelMessage
    paginate_by = 15


class KannelMessageCreateView(CreateView):
    model = KannelMessage

    def get_success_url(self):
        return reverse('message-list')


class KannelMessageDetailView(DetailView):
    model = KannelMessage


class KannelMessageFilterView(FilterView):
    model = KannelMessage

    class Meta:
        fields = ['sender', 'backend', 'created']
        order_by = ['created']
