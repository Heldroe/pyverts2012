from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from middleware.http import Http403

from team360.models import WeekRater, WeekCriterion

@login_required
def home (request):
    ratedlist = WeekRater.objects.filter(rater=request.user, date__gt=datetime.now()-timedelta(weeks=1))
    return render(request, 'team360.html', {'ratedlist': ratedlist})
    
@login_required
def rate (request, user_id):
	ratedlist = WeekRater.objects.filter(rater=request.user, date__gt=datetime.now()-timedelta(weeks=1))
	# if the user doesn't exist, 404 error
	rated_user = get_object_or_404(User, id=user_id)
	ratings=""
	for rated in ratedlist:
		if rated.rated == rated_user:
			ratings = WeekCriterion.objects.filter(date__gt=datetime.now()-timedelta(weeks=1))
	# if user id not authorized to be evaluated by the current user, 403 error
	if ratings == "":
		raise Http403
	return render(request, 'rate.html', {'ratings': ratings})
