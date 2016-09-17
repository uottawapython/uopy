from __future__ import unicode_literals

from django.db import models
from model_utils.models import  TimeStampedModel
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class ClubEvent(TimeStampedModel):
    event_title = models.CharField(max_length=200, verbose_name=_('event_title'))
    event_description = models.CharField(
        max_length=600,
        verbose_name=_('event_description'),
        help_text="Add description " \
                            "Box i.e: This workshop will be about..."
        )
    event_location = models.CharField(max_length=200, verbose_name=_('event_location'))
    event_date = models.DateTimeField(verbose_name=_('event_date'))
    event_duration_min = models.IntegerField( verbose_name=_('event_duration_min'), default=0)
    event_cost = models.IntegerField( verbose_name=_('event_cost'), default=0)
    votes = models.IntegerField( verbose_name=_('votes'), default=0)

    def __str__(self):
        return self.event_title

    class Meta:
        ordering = ['-event_date']
        app_label = 'main'
