from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('foodtruck.views',
	url(r'^$', 'foodtruck_list'),
    url(r'^foodtrucks$', 'foodtruck_list', name='foodtruck_list'),

    url(r'^foodtrucks/(?P<pk>[0-9]+)$', 'foodtruckByID'),
    url(r'^foodtrucks-search-food/(?P<keyword>\w+)$', 'foodtruckByKeyword'),

    url(r'^foodtrucks-search-location/(?P<latitude>\-?\d+(?:\.\d+)?)&(?P<longitude>\-?\d+(?:\.\d+)?)&(?P<radius>\d+(?:\.\d+)?)$',\
    	'foodtruckByLocation'),
    url(r'^foodtrucks-search-location/(?P<latitude>\-?\d+(?:\.\d+)?)&(?P<longitude>\-?\d+(?:\.\d+)?)&(?P<radius>\d+(?:\.\d+)?)&(?P<limit>\d+)$',\
    	'foodtruckByLocation'),
)

urlpatterns = format_suffix_patterns(urlpatterns)