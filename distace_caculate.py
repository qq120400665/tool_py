from math import radians, cos, sin, asin, sqrt
lon1,lat1,lon2,lat2 = map(radians,[121.638481,31.230895,121.551824,31.224058])
print lon1,lat1,lon2,lat2
dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
c = 2 * asin(sqrt(a))  
r = 6371
#print c*r*1000
distance_ = c*r

print distance_