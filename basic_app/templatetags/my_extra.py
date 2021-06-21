from django import template

register = template.Library()

# def cut(value, arg):
#     return value.replace(arg,'')
#
#
# register.filter('cut', cut)


# using the decorator

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg,'')
