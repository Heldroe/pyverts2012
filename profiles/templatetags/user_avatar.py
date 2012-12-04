from django import template

register = template.Library()

@register.inclusion_tag('profiles/avatar_tag.html')
def avatar (avatar_user, size="100"):
    return {'avatar_user': avatar_user, 'size_x': str(size)+"x"+str(size), 'size': size}

@register.inclusion_tag('profiles/avatar_tag_polaroid.html')
def avatar_polaroid (avatar_user, size="100"):
    return {'avatar_user': avatar_user, 'size_x': str(size)+"x"+str(size), 'size': size}