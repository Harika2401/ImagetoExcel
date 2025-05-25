from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def float_format(value, decimal_places):
    return f"{value:.{decimal_places}f}"