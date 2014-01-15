from django.core.urlresolvers import reverse
from django.db import models
from model_utils.models import TimeStampedModel


class KannelMessage(TimeStampedModel):
    backend = models.CharField(max_length=50)
    sender = models.CharField(max_length=16)
    message = models.CharField(max_length=1024)

    def __unicode__(self):
        return 'Message from %s on %s' % (
            self.sender,
            self.backend
        )

    def get_absolute_url(self):
        return reverse('message-view', kwargs={'pk': self.id})

    class Meta:
        get_latest_by = 'created'
