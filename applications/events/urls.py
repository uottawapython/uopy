# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
from django.views.decorators.cache import cache_page
__author__ = 'Guinsly Mondesir'

app_name = 'events'
urlpatterns = [
      #url(r'^event/$', views.Homepage.as_view(), name='events'),
      #url(r'^activite/$', views.Homepage.as_view(), name='activite'),
      url(r'^homepage$', views.homepage, name='index'),
      url(r'^accueil$', views.Accueil),
      url(r'^$', views.hello, name='index'),
        ]
