from django.db import models

from django.contrib.auth.models import User

class Element(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=500)
    
