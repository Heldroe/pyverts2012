from django import template

register = template.Library()

@register.inclusion_tag('elements/photo_thumb.html')
def photo (photo, size="100"):
    return {'photo': photo, 'size_x': str(size)+"x"+str(size), 'size': size}

@register.inclusion_tag('elements/photo_resize.html')
def photo_resize (photo, size="100"):
    return {'photo': photo, 'size': str(size)}

@register.inclusion_tag('elements/photo_swipe.html')
def photo_swipe (photo, size_b="1000", size_t="150"):
    return {'photo': photo,
    		'size_b_x': str(size_b)+"x"+str(size_b),
    	 	'size_b': size_b,
 			'size_t_x': str(size_t)+"x"+str(size_t),
 			'size_t': size_t}