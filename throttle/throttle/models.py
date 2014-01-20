import django_filters

from django.core.urlresolvers import reverse
from django.db import models

from model_utils.models import TimeStampedModel


class KannelMessage(TimeStampedModel):
    backend = models.CharField(max_length=50)
    sender = models.CharField(max_length=16)
    message = models.CharField(max_length=1024)
    handled = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Message from %s on %s' % (
            self.sender,
            self.backend
        )

    def get_absolute_url(self):
        return reverse('message-view', kwargs={'pk': self.id})

    class Meta:
        get_latest_by = 'created'
        ordering = ['-created']


class KannelMessageFilter(django_filters.FilterSet):
    created = django_filters.DateTimeFilter()

    class Meta:
        model = KannelMessage
        fields = ['sender', 'backend', 'created']
        order_by = ['created']
        object_name = 'filter'
