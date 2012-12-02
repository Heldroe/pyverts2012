from django.db import models
from django.contrib.auth.models import User

class Criterion(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

class WeekCriterion(models.Model):
    criterion = models.ForeignKey(Criterion)
    date = models.DateTimeField()

class WeekRater(models.Model):
    rater = models.ForeignKey(User, related_name='weekrater_rater')
    rated = models.ForeignKey(User, related_name='weekrater_rated')
    date = models.DateTimeField()

class Rating(models.Model):
    criterion = models.ForeignKey(Criterion)
    value = models.IntegerField()
    rater = models.ForeignKey(User, related_name='rating_rater')
    rated = models.ForeignKey(User, related_name='rating_rated')
    date = models.DateTimeField()
