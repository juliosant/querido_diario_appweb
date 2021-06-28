from django import template
from django.template import Library

register = Library()

@register.filter(name='formcontrol')
def formcontrol(value, arg):
    return value.as_widget(attrs={'class': arg})