from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'elements.views.list', name='elements_list'),
    url(r'^create/$', 'elements.views.create', name='create_element'),
    url(r'^(?P<element_id>\d+)/$', 'elements.views.view', name='view_element'),
    url(r'^(?P<element_id>\d+)/action/$', 'elements.views.action', name='action_element'),
    url(r'^(?P<element_id>\d+)/recommend/$', 'elements.views.recommend', name='recommend_element'),
    url(r'^(?P<element_id>\d+)/edit/$', 'elements.views.edit', name='edit_element'),
    url(r'^(?P<element_id>\d+)/edit/photos/$', 'elements.views.edit_photos', name='element_edit_photos'),
    url(r'^(?P<element_id>\d+)/edit/photos/cover/(?P<photo_id>\d+)/$', 'elements.views.cover_photo', name='element_cover_photo'),
    url(r'^(?P<element_id>\d+)/edit/photos/main/(?P<photo_id>\d+)/$', 'elements.views.main_photo', name='element_main_photo'),
    url(r'^(?P<element_id>\d+)/edit/photos/delete/(?P<photo_id>\d+)/$', 'elements.views.delete_photo', name='element_delete_photo'),
    url(r'^(?P<element_id>\d+)/edit/photos/add/$', 'elements.views.add_photo', name='element_add_photo'),
    #url(r'^photo/(?P<photo_id>\d+)/$', 'elements.views.view_photo', name='photo_view'),
)
