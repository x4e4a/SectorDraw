import math

def sectors(lat1, lon1, distance, azimuth):
	print(f'lat1 {lat1}')
	print(f'StartLon {lon1}')
	radlat=math.radians(lat1)
	radlon = math.radians(lon1)
	d = distance
	r= 3959.00000 #miles
	print(f'd/r {str(d/r)}')
	print(f'math.cos(d/r) {str(math.cos(d/r))}')
	print(f'math.sin(radlat) {str(math.sin(radlat))}')
	print(f'{lon1},{lat1},0') # Creates the First point as the Point
	for num in range(0,120):
		brng = math.radians((azimuth+300+num)%360) #adjustment made to begin arc for 120 (assumed) sector size
		lat2 = math.asin(math.sin(radlat) * math.cos(d/r) + math.cos(radlat) * math.sin(d/r) * math.cos(brng))			
		lon2 = radlon + math.atan2(math.sin(brng)*math.sin(d/r)*math.cos(radlat), math.cos(d/r)-math.sin(radlat)*math.sin(lat2))
		lat2 = math.degrees(lat2)
		lon2 = math.degrees(lon2)
		print(f'{lon2},{lat2},0')# float,float,0 format of Longitude First, Latitude
	print(f'{lon1},{lat1},0') #Creates the last point to completed the sector (connecting arc to original)

def main():
	sectors(34.722483, -86.584527, 1.34, 90) # StartLat, StartLong, Distance (Miles), Azimuth

main()
