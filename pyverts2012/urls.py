from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pyverts2012.views.home', name='home'),
    #url(r'^user/', include('profiles.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^360/', include('team360.urls')),
    url(r'^elements/', include('elements.urls')),
    # url(r'^pyverts2012/', include('pyverts2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)