from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

@login_required
def my_profile (request):
    return render(request, 'profiles/view.html', {'profile_user': request.user})

def view (request, user_id):
	profile_user = get_object_or_404(User, id=user_id)
	return render(request, 'profiles/view.html', {'profile_user': profile_user})