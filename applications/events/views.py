# -*- coding: utf-8 -*-
#Django
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.views import generic
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
#models
from .models import Event

# Standard Python module
from json import dumps, loads
from datetime import datetime, timedelta

from django.views.generic import TemplateView

import logging
logger = logging.getLogger(__name__)

def Accueil(request):
    logger.info('rendering the homepage')
    return render(
              request,
              'events/home.html',
              {'data': 'hello world'}
            )


def hello_base(request):
    events = Event.objects.all()
    logger.info('rendering the homepage')
    return render(
              request,
              'events/base_amabiblio.html',
              {'events': events}
            )

def hello2(request):
    events = Event.objects.all()
    logger.info('rendering the homepage')
    return render(
              request,
              'events/base_variables.html',
              {'events': events}
            )


def homepage(request):
    logger.info('rendering the homepage')
    return render(
              request,
              'events/base.html',
              {'data': 'hello world'}
            )

def hello(request):
    logger.info('rendering the homepage')
    return render(
              request,
              'events/base.html',
              {'data': 'hello world'}
            )
