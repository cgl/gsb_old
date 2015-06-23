
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from gsb_cal.models import Event
# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView


def index(request):
    response = render_to_response('gsb_cal/index.html')
    return response


class EventList(ListView):
    model = Event #events = Event.objects.all()

class EventDetail(DetailView):
    model = Event
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EventDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['event_list'] = Event.objects.all()
        return context

def get_event_json(request,id):
    event = get_object_or_404(Event, pk=id)
    response = render_to_response('index.html', { 'event': event,})
    return response

"""
def get_as_json(self):
        from django.template.loader import render_to_string
        from django.core.cache import cache
        key = 'get_as_json_' + str(self.id)
        response = cache.get(key)
        timeout = 60 * 60 * 6
        if response:
            return response
        else:
            response = render_to_string('index.html', { 'project': self,})
            cache.set(key, response, timeout)
            return response
"""
