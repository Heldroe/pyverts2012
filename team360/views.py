from datetime import datetime, timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from team360.models import WeekRater

@login_required
def home (request):
    ratedlist = WeekRater.objects.filter(rater=request.user, date__gt=datetime.now()-timedelta(weeks=1))
    return render(request, 'team360.html', {'ratedlist': ratedlist})