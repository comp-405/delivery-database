from django import template

register = template.Library()

@register.simple_tag
def divide(n, d):
  try:
    return "{:.2f}".format((float(n)/float(d)) * 100)
  except (ValueError, ZeroDivisionError):
    return None
