from datetime import datetime, timedelta

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
    ratedlist = WeekRater.objects.filter(rater=request.user, date__gt=datetime.now()-timedelta(weeks=1))
    return render(request, 'team360.html', {'ratedlist': ratedlist})
    
@login_required
def rates (request, user_id):
	ratedlist = WeekRater.objects.filter(rater=request.user, date__gt=datetime.now()-timedelta(weeks=1))
	# if the user doesn't exist, 404 error
	rated_user = get_object_or_404(User, id=user_id)
	ratings=""
	for rated in ratedlist:
		if rated.rated == rated_user:
			if len(Rating.objects.filter(date__gt=datetime.now()-timedelta(weeks=1), rated=User.objects.filter(id=user_id)[0], rater=request.user))==0:
				ratings = WeekCriterion.objects.filter(date__gt=datetime.now()-timedelta(weeks=1))
	# if user id not authorized to be evaluated by the current user, 403 error
	if ratings == "":
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
	



