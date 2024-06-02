from django import template

register = template.Library()

@register.simple_tag
def substract(value, arg):
    print(value, arg)
    return int(value) - int(arg)