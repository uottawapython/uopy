# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _


class Event(TimeStampedModel):
    """
    """
    LANGUAGE_CHOICE = (
            ('FR', 'Francais'),
            ('EN', 'English'),
            )
    MEASURING_CHOICE = (
            ('hr', 'hour'),
            ('hrs', 'hours'),
            ('min', 'minutes'),
            )
    EVENT_CHOICE = (
            ('workshop', 'Workshop'),
            ('atelier', 'Atelier'),
            ('course', 'Course'),
            ('cours', 'Cours'),
            )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(_('Title'),max_length=60, blank=True, null=True)
    start_date = models.DateTimeField(_('Start_date'),auto_now=False, auto_now_add=False, blank=True, null=True, help_text="When do you want to start this workshop.")
    end_date = models.DateTimeField(_('End_date'),auto_now=False, auto_now_add=False, blank=True, null=True, help_text="This is optional")
    duree = models.PositiveIntegerField(_('Duree'),blank=True, null=True, default=45, help_text="How many minutes or hours that this workshop will last.")
    measuring_unit = models.CharField(_('Measuring_unit'),max_length=8, choices=MEASURING_CHOICE, default='minutes')
    language = models.CharField(_('Language'),max_length=2, choices=LANGUAGE_CHOICE, default='En')
    event_type = models.CharField(_('Event_type'),max_length=10, choices=EVENT_CHOICE, default='workshop')
    status = models.CharField(_('Status'),max_length=10, choices=STATUS_CHOICES, default='draft')
    description = models.TextField(_('Description'),blank=True, null=True, help_text="Please write about what user will benefit from subscribing to this Event.")
    photo = models.ImageField(_('Photo'),upload_to='events/%Y/%m/%d', null=True, blank=True)
    #photo = ThumbnailerImageField(upload_to='events/%Y/%m/%d', resize_source=settings.DEFAULT_MASCOTA_IMAGE_SETTING, blank=True, null=True)
    slug = models.CharField(_('Slug'),max_length=200)
    tags = TaggableManager(blank=True, help_text='Enter the Comma separated Taxonomy', verbose_name="标签", related_name="taxonomy")


    def __str__(self):
        return 'Title: {}'.format(self.title)
    '''
    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'slug': self.slug})
    '''

    class Meta:
        app_label = 'events'
        verbose_name = 'activities'
        verbose_name_plural = 'activities'
        ordering = ('-created', )
