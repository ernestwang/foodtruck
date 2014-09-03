from decimal import *
import numpy as ny
import math

LAT_PER_MILE = 0.0145#Decimal(0.0145) # approximate difference in degree of latitude per mile
LON_PER_MILE = 0.0189#Decimal(0.0189) # approximate difference in degree of longitude per mile
RADIUS_EARTH = 3963#Decimal(3963)

def haversine(phi, psi):
	dsine = ny.sin(phi[:,0] - psi[0])
	pcos = ny.cos(psi[0])*ny.cos(phi[:,0])
	phi = ny.deg2rad(phi)
	psi = ny.deg2rad(psi)
	return 2 * RADIUS_EARTH * ny.arcsin(ny.sqrt(ny.sin((phi[:,0] - psi[0])/2 ) ** 2 + ny.cos(psi[0])*ny.cos(phi[:,0]) * ny.sin((-psi[1] + phi[:, 1])/2) **2))


fts = [(37.7841781654502, -122.3940641),(37.7800057164663, -122.39027096130),(37.7862060958787, -122.4025324913)]
n = len(fts)

ft_coords = ny.zeros((3,2))#	,dtype=ny.dtype(Decimal))
for i, ft in enumerate(fts):
	print fts[i] 
	print ","
	ft_coords[i,0] = Decimal(fts[i][0])
	ft_coords[i,1] = Decimal(fts[i][1])
	print type(ft_coords[i,0])
curr_coords = ny.array([37.77755, -122.39099])#,dtype=ny.dtype(Decimal))
dist = haversine(ft_coords, curr_coords)

print dist
print fts
fts = [ft for (d, ft) in sorted(zip(dist, fts))]
dist = [d for (d, ft) in sorted(zip(dist, fts))]
print dist
print fts