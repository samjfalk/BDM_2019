import sys
import json
import csv

if __name__=='__main__':
    with open(sys.argv[1], 'r') as fi, \
         open(sys.argv[2], 'w') as fo:
        writer = csv.writer(fo)
        writer.writerow(['Station Name', 'Latitude', 'Longitude'])
        data = json.load(fi)
        stations = data['stationBeanList']
        for s in stations:
            if s['statusKey']==3:  
                stationName = s['stationName']
                stationLat  = s['latitude']
                stationLon  = s['longitude']
                writer.writerow((stationName, stationLat, stationLon))

