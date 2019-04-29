from django import template

register = template.Library()

@register.simple_tag
def divide(n, d):
  try:
    return "{:.2f}".format((int(n)/int(d)) * 100)
  except (ValueError, ZeroDivisionError):
    return None
