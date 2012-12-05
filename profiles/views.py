# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.contrib.auth.models import User

from profiles.models import UserProfile
from profiles.forms import ProfileEditForm, ProfileAvatarForm

from actstream import action
from actstream.models import actor_stream, user_stream
from actstream.actions import follow, unfollow

from django.utils.translation import ugettext as _

from haystack.query import SearchQuerySet
from django.views.decorators.csrf import csrf_exempt

import json

@login_required
def my_profile (request):
    return view(request, request.user.id)

def view (request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    profile_stream = actor_stream(profile_user)
    return render(request, 'profiles/view.html', {'profile_user': profile_user,
                                                  'profile_stream': profile_stream})

def follow_profile (request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    follow(request.user, profile_user, send_action=False)
    action.send(request.user, verb=_(u"suit désormais"), target=profile_user)
    return redirect(profile_user.get_profile())

def usersearch (request, query=""):
    if request.method == 'GET':
        query = request.GET['q']
    print query
    results = SearchQuerySet().autocomplete(profile=query)
    names = []
    for nr in results:
        names.append(nr.object.user.username)
    return HttpResponse(json.dumps({'usernames': names}))

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
                action.send(request.user, verb=_(u"a modifié sa description"))
        elif 'avatar_form' in request.POST:
            avatar_form = ProfileAvatarForm(request.POST, request.FILES, instance=profile)
            if avatar_form.is_valid():
                profile = avatar_form.save(commit=False)
                profile.save()
                action.send(request.user, verb=_(u"a modifié sa photo de profil"))
    return render(request, 'profiles/edit.html', {'base_form': base_form,
                                                  'avatar_form': avatar_form})