from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ClubEvent(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.CharField(max_length=600)
    event_location = models.CharField(max_length=200)
    event_date = models.DateTimeField('event date')    
    event_duration_min = models.IntegerField(default=0)
    event_cost = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.event_title
