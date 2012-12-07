from django.conf.urls import patterns, include, url
from team360.views import home, rates, rate

urlpatterns = patterns('',
    url(r'^$', 'team360.views.home', name='team360_home'),
    url(r'^rate/(?P<user_id>\d+)/$', 'team360.views.rates', name='team360_rates'),
    url(r'^rate/(?P<user_id>\d+)/(?P<criterion_id>\d+)/$', 'team360.views.rate', name='team360_rate'),
)
