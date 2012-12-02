from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    test = models.CharField(max_length=20, default="Dragons.")
