from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def lower(value):
	return value.lower()

#def cut(value, arg):
#    """Removes all values of arg from the given string"""
#    return value.replace(arg, '')
#
#def lower(value): # Only one argument.
#    """Converts a string into all lowercase"""
#    return value.lower()
#
#register.filter('cut', cut)
#register.filter('lower', lower)

@register.filter(is_safe=True)
def myfilter(value):
    return value 

@register.filter(is_safe=True)
def add_xx(value):
    return '%sxx' % value 