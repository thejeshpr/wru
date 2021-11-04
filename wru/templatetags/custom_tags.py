from django import template

register = template.Library()

@register.simple_tag
def get_place_icon():
    return "las la-map-marker"


@register.simple_tag
def get_entry_icon():
    return "las la-list-ol"


@register.simple_tag
def get_feeling_icon():
    return "las la-grin-squint"