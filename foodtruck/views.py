from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from foodtruck.models import FoodTruck
from foodtruck.serializers import FoodTruckSerializer
from decimal import *
import numpy as ny

LAT_PER_MILE = Decimal(0.0145) # approximate difference in degree of latitude per mile
LON_PER_MILE = Decimal(0.0189) # approximate difference in degree of longitude per mile
RADIUS_EARTH = 3963

@api_view(['GET', 'POST'])
def foodtruck_list(request):
	print "foodtruck_list"
	"""
	List all foodtrucks, or create a new foodtruck.
	"""
	if request.method == 'GET':
		foodtrucks = FoodTruck.objects.all()
		serializer = FoodTruckSerializer(foodtrucks, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = FoodTruckSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def foodtruckByID(request, pk, format=None):
	print "foodtruckByID"
	"""
	Retrieve, update or delete a foodtruck instance.
	"""
	try:
		foodtruck = FoodTruck.objects.get(objectid=pk)
	except FoodTruck.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = FoodTruckSerializer(foodtruck)
		return Response(serializer.data)

	elif request.method == 'PUT':
	    serializer = FoodTruckSerializer(foodtruck, data=request.DATA)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
	    foodtruck.delete()
	    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def foodtruckByKeyword(request, keyword, format=None):
	print "foodtruckByID"
	"""
	Retrieve, update or delete a foodtruck instance.
	"""

	foodtrucks = FoodTruck.objects.filter(Q(applicant__icontains=keyword) | Q(foodItems__icontains=keyword))

	if request.method == 'GET':
		serializer = FoodTruckSerializer(foodtrucks, many=True)
		return Response(serializer.data)

	elif request.method == 'PUT':
	    serializer = FoodTruckSerializer(foodtrucks, data=request.DATA, many=True)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		for foodtruck in foodtrucks:
		    foodtruck.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def foodtruckByLocation(request, latitude, longitude, radius, limit=15, format=None):
	print "foodtruckByLocation"
	"""
		Retrieve foodtrucks nearby a given location, the default limit of 
		search is 15
	"""
	lat = Decimal(latitude)
	lon = Decimal(longitude)
	radius = Decimal(radius)
	#limit = Decimal(limit)
	
	foodtrucks = FoodTruck.objects.filter(latitude__range=(lat-radius*LAT_PER_MILE, lat+radius*LAT_PER_MILE),\
									longitude__range=(lon-radius*LON_PER_MILE, lon+radius*LON_PER_MILE))
	n = len(foodtrucks)
	if n > 0:
		ft_coords = ny.zeros((n, 2))
		for (i, ft) in enumerate(foodtrucks):
			ft_coords[i,0] = ft.latitude
			ft_coords[i,1] = ft.longitude

		curr_coords = ny.array([float(latitude), float(longitude)])
		dist = haversine(ft_coords, curr_coords)
		foodtrucks = [ft for (d, ft) in sorted(zip(dist, foodtrucks))]
		foodtrucks = foodtrucks[0:int(limit)]
	if request.method == 'GET':
		serializer = FoodTruckSerializer(foodtrucks, many=True)
		return Response(serializer.data)

def haversine(coord1, coord2):
	"""
	compute the haversine distance between a list coordinates (coord1) and a given coordinate (coord2)
	"""
	return 2 * RADIUS_EARTH * ny.arcsin(ny.sqrt(ny.sin((coord1[:,0] - coord2[0])/2 ) ** 2 + ny.cos(coord2[0])*ny.cos(coord1[:,0]) * ny.sin((coord2[1] -coord1[:,1])/2) **2))
