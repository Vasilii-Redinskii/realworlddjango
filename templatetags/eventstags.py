from django import template
from django.template import defaultfilters

register = template.Library()


@register.filter
def eventsdate(date):
    return defaultfilters.date(date, "d.m.Y в G:i")