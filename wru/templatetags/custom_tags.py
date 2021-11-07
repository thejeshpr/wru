from django import template

register = template.Library()


@register.simple_tag
def get_brand_icon():
    return "las la-globe"


@register.simple_tag
def get_place_icon():
    return "las la-map-marked-alt"

@register.simple_tag
def get_entry_icon():
    return "las la-list-ol"


@register.simple_tag
def get_feeling_icon():
    return "las la-grin-squint"


@register.simple_tag
def get_tag_icon():
    return "las la-tags"


@register.simple_tag
def get_created_at_icon():
    return "las la-calendar-day"