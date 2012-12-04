from django import template

register = template.Library()

@register.inclusion_tag('profiles/bootstrap_action.html')
def bootstrap_action (action):
    return {'action': action}