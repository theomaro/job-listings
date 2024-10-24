from django import template
from datetime import datetime


register = template.Library()


@register.filter
def days_until(date):
    delta = datetime.now().date() - datetime.date(date)
    return delta.days
