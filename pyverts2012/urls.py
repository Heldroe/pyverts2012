from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pyverts2012.views.home', name='home'),
    url(r'^search/$', 'pyverts2012.views.search', name='search'),
    url(r'^discover/$', 'pyverts2012.views.discover', name='discover'),
    url(r'^theme/(?P<new_theme>.*)/$', 'pyverts2012.views.theme', name='theme'),
    url(r'^profile/', include('profiles.urls')),
    url(r'^360/', include('team360.urls')),
    url(r'^elements/', include('elements.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^activity/', include('actstream.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)