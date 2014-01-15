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

    class Meta:
        get_latest_by = 'created'
