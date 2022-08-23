import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from events.models import Event, Feature, Category


# Create your views here.

def index(request):
    return HttpResponse('Hello, World')


def event_list(request):
    template_name = 'events/event_list.html'
    event_objects = Event.objects.all()
    category_objects = Category.objects.all()
    feature_objects = Feature.objects.all()

    context = {
        'event_objects': event_objects,
        'category_objects': category_objects,
        'feature_objects': feature_objects,
        'user': request.user,

    }
    return render(request, template_name, context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event': event,
    }
    return render(request, 'events/event_detail.html', context)
