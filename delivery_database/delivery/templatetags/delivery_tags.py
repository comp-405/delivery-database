from django import template

register = template.Library()

@register.simple_tag
def divide(n, d):
  try:
    return float(n) / float(d)
  except (ValueError, ZeroDivisionError):
    return None