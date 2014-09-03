from django.test import TestCase
from foodtruck.models import FoodTruck
from dateutil.parser import parse
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from decimal import *

class FoodTruckSimpleTestCase(TestCase):
	
	def setUp(self):
		FoodTruck.objects.create(objectid=0, applicant='dummy0')
		FoodTruck.objects.create(objectid=1, applicant='dummy1', facilitytype='Push Cart')


	def test_foodtrucks_applicant(self):
		dummy0 = FoodTruck.objects.get(applicant='dummy0')
		dummy1 = FoodTruck.objects.get(applicant='dummy1')
		self.assertEqual(dummy0.applicant, 'dummy0')
		self.assertEqual(dummy1.applicant, 'dummy1')

	def test_foodtrucks_defaultvalues(self):
		dummy0 = FoodTruck.objects.get(applicant='dummy0')
		dummy1 = FoodTruck.objects.get(applicant='dummy1')
		self.assertEqual(dummy0.facilitytype, 'Truck')
		self.assertEqual(dummy1.facilitytype, 'Push Cart')

	def test_foodtrucks_integrity(self):
		self.assertRaises(IntegrityError, FoodTruck.objects.create, objectid=0)

class FoodTruckAPITestCase(APITestCase):

	def test_foodtrucks_create(self):
		"""
		Make sure can create a new foodtruck
		"""
		url = reverse('foodtruck_list')
		data = {"status" : "APPROVED",\
		  "expirationdate" : "2015-03-15T00:00:00",\
		  "permit" : "14MFF-0107",\
		  "block" : "3794",\
		  "received" : "Jun 24 2014  1:49PM",\
		  "facilitytype" : "Truck",\
		  "blocklot" : "3794002A",\
		  "locationdescription" : "02ND ST: TOWNSEND ST to KING ST (700 - 799)",\
		  "cnn" : 148000,\
		  "priorpermit" : 1,\
		  "approved" : "2014-06-24T13:55:30",\
		  "noisent" : "2013-07-25T00:00:00",\
		  "schedule" : "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=14MFF-0107&ExportPDF=1&Filename=14MFF-0107_schedule.pdf",\
		  "address" : "750 02ND ST",\
		  "applicant" : "Steve's Mobile Deli",\
		  "lot" : "002A",\
		  "fooditems" : "Cold Truck: Pre-packaged sandwiches: Burgers: Hot Dogs: Muffin Sandwiches: Enchiladas: Bagels: Burritos: Salads: Snacks: Beverages",\
		  "longitude" : -122.402978526686,\
		  "latitude" : 37.7302216813049, \
		  "y" : 2093947.369,\
		  "x" : 6011371.493,\
		  "objectid" : 554527}
		
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		quant = '1.000000'
		for k, v in data.iteritems():
			if v is not None and (k is "y" or k is "x" or k is "latitude" or k is "longitude"):
				self.assertEqual(response.data[k].quantize(Decimal(quant)), Decimal(v).quantize(Decimal(quant)))
			elif v is not None and (k is "approved" or k is "received" or k is "expirationdate" or k is "noisent"):
				self.assertEqual(response.data[k], parse(v))
			else:
				self.assertEqual(response.data[k], v)
		
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		for k, v in data.iteritems():
			if v is not None and (k is "y" or k is "x" or k is "latitude" or k is "longitude"):
				self.assertEqual(response.data[0][k].quantize(Decimal(quant)), Decimal(v).quantize(Decimal(quant)))
			elif v is not None and (k is "approved" or k is "received" or k is "expirationdate" or k is "noisent"):
				self.assertEqual(response.data[0][k], parse(v))
			else:
				self.assertEqual(response.data[0][k], v)
		

	def test_foodtrucks_searchByID(self):
		"""
		Test retrieving, updating and deleting foodtruck record by ID
		"""
		url = reverse('foodtruck_list')
		data = {'objectid': 2, 'x': 1.0, 'y': 1.5}
		response = self.client.post(url, data, format='json')
		#print response.status_code
		response = self.client.get('/foodtrucks/2', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['objectid'], 2)
		self.assertEqual(response.data['x'], 1.0)
		self.assertEqual(response.data['y'], 1.5)

		data = {'objectid': 2, 'x': 1.0, 'y': 2.0}
		response = self.client.put('/foodtrucks/2', data, format='json')
		response = self.client.get('/foodtrucks/2', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['y'], 2.0)

		response = self.client.delete('/foodtrucks/2', format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		

	def test_foodtrucks_searchByKeyword(self):
		"""
		Test retrieving, updating and deleting foodtruck record by keyword
		"""
		url = reverse('foodtruck_list')
		data0 = {'objectid': 0, 'applicant':'Pizza', 'x': 0.0, 'y': 0.5}
		data1 = {'objectid': 1, 'applicant':'Chicago', 'fooditems': 'deep dish pizza and sandwiches', 'x': 1.0, 'y': 1.0}
		data2 = {'objectid': 2, 'applicant':'hotdog house', 'x': 1.5, 'y': 1.5}
		response = self.client.post(url, data0, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response = self.client.post(url, data1, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response = self.client.post(url, data2, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		#print response.status_code
		response = self.client.get('/foodtrucks/bykeyword?keyword=pizza', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 2)
		self.assertEqual(response.data[0]['objectid'], 0)
		self.assertEqual(response.data[1]['objectid'], 1)

		
	
	def test_foodtrucks_searchByLocation(self):
		"""
		Test retrieving,  foodtrucks nearby
		"""

		url = reverse('foodtruck_list')
		data = [{'objectid': 0,  'latitude':37.7841781516735  , 'longitude':-122.394064145441 },\
				{'objectid': 1,  'latitude':37.7862060821039  , 'longitude':-122.402532491346 },  	#ft2 is closest to ft0\
				{'objectid': 2,  'latitude':37.7800057026855  , 'longitude':-122.390270961311 },	#ft1 is further to ft0\
				{'objectid': 3,  'latitude':32  , 'longitude': -100}]								#ft3 is far far away
		for d in data:
			response = self.client.post(url, d, format='json')
			self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
		lat = data[0]['latitude']   #given latitude
		lon = data[0]['longitude']	#given longitude
		rad = 3 					#given radius of search
		lim = 2 					#given limit of results
		""" test both urls: w/ or w/out limit """
		response = self.client.get('/foodtrucks/bylocation?latitude=%f&longitude=%f&radius=%f' % (lat, lon, rad), format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 3)
		self.assertEqual(response.data[0]['objectid'], 0)
		self.assertEqual(response.data[1]['objectid'], 2)		
		self.assertEqual(response.data[2]['objectid'], 1)		

		response = self.client.get('/foodtrucks/bylocation?latitude=%f&longitude=%f' % (lat, lon), format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 3)

		response = self.client.get('/foodtrucks/bylocation?latitude=%f&longitude=%f&radius=%f&limit=%d' % (lat, lon, rad, lim), format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 2)

		""" test the radius: shrink the radius such that only ft0 will be found """
		rad = 0.01
		response = self.client.get('/foodtrucks/bylocation?latitude=%f&longitude=%f&radius=%f' % (lat, lon, rad), format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

class FoodTruckStressTestCase(APITestCase):
	"""
	Test the throughput
	"""
	def setUp(self):
		pass