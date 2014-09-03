from foodtruck.models import FoodTruck
from foodtruck.serializers import FoodTruckSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from  django.db import IntegrityError
import json
import urllib2
from dateutil.parser import parse

def getValue (m, key):
	if key in m:
		return m[key]
	else:
		return None

def parseDate( str):
	if str is None:
		return None
	else:
		return parse(str)

data = urllib2.urlopen('http://data.sfgov.org/resource/rqzj-sfat.json')
ftinfo = json.load(data)

for info in ftinfo:
	print info['objectid']
	objectid = getValue(info, 'objectid')
	applicant = getValue(info, 'applicant')
	facilitytype = getValue(info, 'facilitytype')
	cnn = getValue(info, 'cnn')
	locationdescription = getValue(info, 'locationdescription')
	address = getValue(info, 'address')
	blocklot = getValue(info, 'blocklot')
	block = getValue(info, 'block')
	lot = getValue(info, 'lot')
	permit = getValue(info, 'permit')
	status = getValue(info, 'status')
	foodItems = getValue(info, 'fooditems')
	x = getValue(info, 'x')
	y = getValue(info, 'y')
	latitude = getValue(info, 'latitude')
	longitude = getValue(info, 'longitude')
	schedule = getValue(info, 'schedule')
	priorPermit = getValue(info, 'priorpermit')
	noisent = parseDate(getValue(info, 'noisent'))
	approved = parseDate(getValue(info, 'approved'))
	received = parseDate(getValue(info, 'received'))
	expirationDate = parseDate(getValue(info, 'expirationdate'))

	ft = FoodTruck( objectid=objectid ,  applicant=applicant ,  facilitytype=facilitytype ,  \
					cnn=cnn ,  locationdescription=locationdescription ,  address=address ,\
					blocklot=blocklot ,  block=block ,  lot=lot , permit=permit ,  \
					status=status ,  foodItems=foodItems ,  x=x ,  y=y ,\
					latitude=latitude ,  longitude=longitude ,  schedule=schedule ,\
					priorPermit=priorPermit ,  noisent=noisent ,  approved=approved ,\
					received=received ,  expirationDate=expirationDate )
	try:
		ft.save()
	except IntegrityError as e:
		pass
