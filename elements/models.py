from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

from sorl.thumbnail import ImageField

class Element(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=500)
    original_avatar = models.ImageField(upload_to='elements/avatars/')
    avatar = ImageSpecField([ResizeToFill(200, 200)],
                format='JPEG', options={'quality': 90})

    def get_absolute_url(self):
        return reverse('elements.views.view', args=[str(self.id)])

class Photo(models.Model):
    element = models.ForeignKey(Element)
    picture = ImageField(upload_to='element_photos')
    main = models.BooleanField(default=False)
    cover = models.BooleanField(default=False)
    title = models.CharField(max_length=140, blank=True, default="")
    description = models.CharField(max_length=500, blank=True, default="")

    def __unicode__(self):
        if len(self.title) > 0:
            return self.title
        else:
            return u'Photo #%s' % str(self.id)
