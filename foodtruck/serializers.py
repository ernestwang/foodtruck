from django.forms import widgets
from rest_framework import serializers
from foodtruck.models import FoodTruck
from code_challenge.settings import *

class FoodTruckSerializer(serializers.ModelSerializer):
	approved = serializers.DateTimeField(input_formats=DATETIME_INPUT_FORMATS, blank=True, required=False)
	received = serializers.DateTimeField(input_formats=DATETIME_INPUT_FORMATS, blank=True, required=False)
	expirationDate = serializers.DateTimeField(input_formats=DATETIME_INPUT_FORMATS, blank=True, required=False)
	noisent = serializers.DateTimeField(input_formats=DATETIME_INPUT_FORMATS, blank=True, required=False)
	class Meta:
		model = FoodTruck
		fields = ('objectid',	'applicant', 'facilitytype', 'cnn', 'locationdescription', 'address', 'blocklot', 'block', \
				'lot', 'permit', 'status', 'fooditems', 'x', 'y', 'latitude', 'longitude', 'schedule', 'priorpermit',\
				'approved', 'received', 'expirationdate', 'noisent')