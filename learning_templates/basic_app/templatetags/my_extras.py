from django import template

register = template.Library()

@register.filter('cut')
def cut(value,arg):
    """
    This will remove arg with blank in string
    """
    return value.replace(arg, '')

# register.filter('cut',cut)
