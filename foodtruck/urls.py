from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('foodtruck.views',
	url(r'^$', 'foodtruck_list'),
    url(r'^foodtrucks/$', 'foodtruck_list', name='foodtruck_list'),

    url(r'^foodtrucks/(?P<pk>[0-9]+)$', 'foodtruckByID'),
    url(r'^foodtrucks/bykeyword$', 'foodtruckByKeyword'),

    url(r'^foodtrucks/bylocation$','foodtruckByLocation'),
    #url(r'^foodtrucks/bylocation/latitude=(?P<latitude>\-?\d+(?:\.\d+)?)&longitude=(?P<longitude>\-?\d+(?:\.\d+)?)&radius=(?P<radius>\d+(?:\.\d+)?)&limit=(?P<limit>\d+)$',\
    #	'foodtruckByLocation'),
)

urlpatterns = format_suffix_patterns(urlpatterns)