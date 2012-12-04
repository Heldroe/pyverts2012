from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'profiles.views.my_profile', name='my_profile'),
    url(r'^edit/$', 'profiles.views.edit', name='edit_profile'),
    url(r'^(?P<user_id>\d+)/$', 'profiles.views.view', name='view_profile'),
    url(r'^(?P<user_id>\d+)/follow/$', 'profiles.views.follow_profile', name='follow_profile'),
)
