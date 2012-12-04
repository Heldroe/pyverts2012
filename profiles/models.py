from django.db import models
from django.db.models.signals import post_save
from sorl.thumbnail import ImageField

from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    avatar = ImageField(upload_to='profile_avatar', null=True)
    test = models.CharField(max_length=20, default="Dragons.")

    def get_absolute_url(self):
    	return reverse('profiles.views.view', args=[str(self.id)])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)