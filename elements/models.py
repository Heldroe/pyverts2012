from django.db import models

from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

class Element(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=500)
    avatar = ImageSpecField([ResizeToFill(200, 200)],
                format='JPEG', options={'quality': 90})
    
