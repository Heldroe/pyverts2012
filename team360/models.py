from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime

class Criterion(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    def __unicode__(self):
        return self.name

class WeekCriterion(models.Model):
    criterion = models.ForeignKey(Criterion)
    date = models.DateTimeField()
    def __unicode__(self):
        return unicode(self.criterion)

class WeekRater(models.Model):
    rater = models.ForeignKey(User, related_name='weekrater_rater')
    rated = models.ForeignKey(User, related_name='weekrater_rated')
    date = models.DateTimeField()
    def __unicode__(self):
        return unicode(self.rater)

class Rating(models.Model):
	BAR_CHOICES = (
        (0, "Mauvais"),
        (1, "Mediocre"),
        (2, "Moyen"),
        (3, "Bien"),
    )
	criterion = models.ForeignKey(Criterion)
	value = models.IntegerField(blank=True, null=True, choices=BAR_CHOICES)
	rater = models.ForeignKey(User, related_name='rating_rater')
	rated = models.ForeignKey(User, related_name='rating_rated')
	date = models.DateTimeField()
	def __unicode__(self):
		return unicode(self.rater)
		
def allocate_ratings(sender, instance, created, **kwargs):
    if created:
    	# we take 10 people from members and make the newly created user able to rate them
    	for user in User.objects.exclude(id=instance.id).order_by('?')[:10]:
    		WeekRater.objects.create(rated=user, rater=instance, date=datetime.now())

post_save.connect(allocate_ratings, sender=User)
