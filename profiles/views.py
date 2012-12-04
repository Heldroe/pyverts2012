from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.contrib.auth.models import User

from profiles.models import UserProfile
from profiles.forms import ProfileEditForm, ProfileAvatarForm

@login_required
def my_profile (request):
    return render(request, 'profiles/view.html', {'profile_user': request.user})

def view (request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    return render(request, 'profiles/view.html', {'profile_user': profile_user})

@login_required
def edit (request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist: # profile creation failed
        profile = UserProfile.objects.create(user=request.user)

    base_form = ProfileEditForm(instance=profile)
    avatar_form = ProfileAvatarForm(instance=profile)
    if request.method == "POST":
        if 'base_form' in request.POST:
            base_form = ProfileEditForm(request.POST, instance=profile)
            if base_form.is_valid():
                profile = base_form.save(commit=False)
                profile.save()
        elif 'avatar_form' in request.POST:
            avatar_form = ProfileAvatarForm(request.POST, request.FILES, instance=profile)
            if avatar_form.is_valid():
                profile = avatar_form.save(commit=False)
                profile.save()
    return render(request, 'profiles/edit.html', {'base_form': base_form,
                                                  'avatar_form': avatar_form})