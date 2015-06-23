"""gsb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls

from gsb_cal.views import index, get_event_json, EventList, EventDetail

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^events/$', EventList.as_view(), name='event-list'),
    url(r'^events/(?P<slug>[-\w]+)/$', EventDetail.as_view(), name='event-detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ws/event/(?P<id>[\d]+)/$', get_event_json),
    url(r'^admindocs/', include(admindocs_urls))

]
