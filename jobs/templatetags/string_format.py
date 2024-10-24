from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def map_to_list(text: str):
    newStr = text.splitlines()
    return [f"{x}" for x in newStr if x]
