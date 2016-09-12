from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import ClubEvent


def index(request):
    event_list = ClubEvent.objects.order_by('event_date')
    context = {'event_list': event_list}
    return render(request, 'main/index.html', context)
