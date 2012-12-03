from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'team360.views.home', name='team360_home'),
    url(r'^(?P<user_id>\d+)/$', 'team360.views.rate', name='team360_rate'),
)
