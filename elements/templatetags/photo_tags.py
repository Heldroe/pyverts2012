from django import template

register = template.Library()

@register.inclusion_tag('elements/photo_thumb.html')
def photo (photo, size="100"):
    return {'photo': photo, 'size_x': str(size)+"x"+str(size), 'size': size}