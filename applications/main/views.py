from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from .models import ClubEvent
import logging
logger = logging.getLogger(__name__)

class HomeView(ListView):
    """
    Root url of uopy.ca
    return a list of all upcoming events.
    """
    model = ClubEvent
    template_name = 'main/index.html'
    #ordering = '-event_date'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['event_list'] = ClubEvent.objects.order_by('event_date')
        return context

'''
TODO: to implement later

def handler404(request):
    response = render(request, 'main/page_not_found.html')
    logger.info('Error page not found 404')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, 'server_error.html')
    logger.info('main/Error page not found 500')
    response.status_code = 500
    return response
'''
