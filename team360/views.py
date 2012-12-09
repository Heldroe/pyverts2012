from datetime import datetime, timedelta
from operator import itemgetter

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from middleware.http import Http403

from team360.models import WeekRater, WeekCriterion, Rating, Criterion
from team360.forms import RateUserForm

@login_required
def home (request):
	# list of people to be noted by the user
	ratedlist = WeekRater.objects.filter(rater=request.user, date__gt=datetime.now()-timedelta(weeks=1))
	ratedlist_final = []
	for rated in ratedlist:
		if len(Rating.objects.filter(date__gt=datetime.now()-timedelta(weeks=1), rated=rated.rated, rater=request.user)) < len(WeekCriterion.objects.filter(date__gt=datetime.now()-timedelta(weeks=1))):
			ratedlist_final.append(rated)
	# fame rating
	famelist = []
	famenotelist = []
	user_ratings = {}
	user_ratings_number = {}
	i=0
	for rate in Rating.objects.all():
		if rate.rated.id in user_ratings:
			user_ratings[rate.rated.id] += rate.value
		else:
			user_ratings[rate.rated.id] = rate.value
		if rate.rated.id in user_ratings_number:
			user_ratings_number[rate.rated.id] += 1
		else:
			user_ratings_number[rate.rated.id] = 1
		i += 1
	for k in user_ratings.keys():
		user_ratings[k] = float(user_ratings[k])/float(user_ratings_number[k])
	user_ratings = sorted(user_ratings.items(), key=itemgetter(1), reverse=True)
	print(user_ratings)
	for note in user_ratings:
		famelist.append(User.objects.get(pk=note[0]))
		famenotelist.append(note[1])
	liste = zip(famelist, famenotelist)
	return render(request, 'team360.html', {'ratedlist': ratedlist_final, 'famelist': liste})
    
@login_required
def rates (request, user_id):
	ratedlist = WeekRater.objects.filter(rater=request.user, date__gt=datetime.now()-timedelta(weeks=1))
	# if the user doesn't exist, 404 error
	rated_user = get_object_or_404(User, id=user_id)
	ratings=[]
	for rated in ratedlist:
		if rated.rated == rated_user:
			for crit in WeekCriterion.objects.filter(date__gt=datetime.now()-timedelta(weeks=1)):
				if len(Rating.objects.filter(date__gt=datetime.now()-timedelta(weeks=1), rated=User.objects.filter(id=user_id)[0], rater=request.user, criterion=crit))==0:
					ratings.append(crit)
	# if user id not authorized to be evaluated by the current user, 403 error
	if ratings == []:
		raise Http403
	return render(request, 'rates.html', {'rated_user': rated_user, 'ratings': ratings})

@login_required
def rate (request, user_id, criterion_id):
	form = RateUserForm(instance=Rating(rated=User.objects.filter(id=user_id)[0], rater=request.user, criterion=Criterion.objects.filter(id=criterion_id)[0]))
	if request.method == "POST":
		form = RateUserForm(request.POST, instance=Rating(rated=User.objects.filter(id=user_id)[0], rater=request.user, criterion=Criterion.objects.filter(id=criterion_id)[0], date=datetime.now()))
        if form.is_valid():
			form.save()
			return redirect(reverse("team360.views.home"))
	else:
		form = RateUserForm(instance=Rating(rated=User.objects.filter(id=user_id)[0], rater=request.user, criterion=Criterion.objects.filter(id=criterion_id)[0]))
	return render(request, 'rate.html', {'user_id' : user_id, 'criterion_id' : criterion_id, 'form': form})
	



