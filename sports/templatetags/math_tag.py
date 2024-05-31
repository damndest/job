from django import template

register = template.Library()

@register.simple_tag
def substract(value, arg):
    return value - arg