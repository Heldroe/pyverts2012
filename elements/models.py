from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from sorl.thumbnail import ImageField

class Category(models.Model):
    name = models.CharField(max_length=200)
    plural = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000)
    verb_singular = models.CharField(max_length=100)
    verb_plural = models.CharField(max_length=100)
    verb_plural_plural = models.CharField(max_length=100)
    picture = ImageField(upload_to='category_photos', blank=True)
    def __unicode__(self):
        return self.plural


class Element(models.Model): #def process(id, uri, name, descr, depiction, latitude, longitude):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=5000)
    category = models.ForeignKey(Category, default=1)

    db_uri = models.CharField(max_length=5000, blank=True, default="")
    db_id = models.CharField(max_length=200, blank=True, default="")
    db_img = models.CharField(max_length=2000, blank=True, default="", null=True)
    latitude = models.CharField(max_length=200, blank=True, default="")
    longitude = models.CharField(max_length=200, blank=True, default="")

    def get_absolute_url(self):
        return reverse('elements.views.view', args=[str(self.id)])

    def __unicode__(self):
        return self.name

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

class ElementRecommendation(models.Model):
    user = models.ForeignKey(User)
    element = models.ForeignKey(Element)

class ElementAction(models.Model):
    user = models.ForeignKey(User)
    element = models.ForeignKey(Element)
