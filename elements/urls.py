from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'elements.views.list', name='elements_list'),
    url(r'^create/$', 'elements.views.create', name='create_element'),
    url(r'^(?P<element_id>\d+)/$', 'elements.views.view', name='view_element'),
    url(r'^edit/(?P<element_id>\d+)/$', 'elements.views.edit', name='edit_element'),
)
