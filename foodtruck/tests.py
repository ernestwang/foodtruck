from django.test import TestCase
from foodtruck.models import FoodTruck
from dateutil.parser import parse
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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
	"""
	def test_foodtrucks_datetime(self):
		dummy2 = FoodTruck.objects.get(objectid=2)
		self.assertEqual(dummy2.approved, parse(date1))
		self.assertEqual(dummy2.received, parse(date2))
		self.assertEqual(dummy2.expirationDate, parse(date3))
		self.assertIsNone(dummy2.noisent)
	"""
	def test_foodtrucks_integrity(self):
		self.assertRaises(IntegrityError, FoodTruck.objects.create, objectid=0)

class FoodTruckAPITestCase(APITestCase):
	def test_foodtrucks_create(self):
		"""
		Make sure can create a new foodtruck
		"""
		url = reverse('foodtruck_list')
		data = {'objectid': 1}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data['objectid'], data['objectid'])

		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data[0]['objectid'], data['objectid'])

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
		