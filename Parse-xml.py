# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import csv

tree = ET.ElementTree(file='Air quality - Queensland.xml')
root = tree.getroot()

# Select region tag
regions = root[0]
for region in regions:
    print(region.tag, region.attrib['name'])

# Parse station element
rows = []

for region in regions:
    region_keys = list(region.attrib.keys())
    for station in region:
        print(station.tag, station.attrib['name'])
        station_keys = list(station.attrib.keys())
        for measurement in station:
            print(measurement.tag, measurement.attrib)
            measurement_keys = list(measurement.attrib.keys())
            
            region_name = region.attrib['name']
            station_name = station.attrib['name']
            measurement_item = measurement.attrib['name']
            measurement_rating = measurement.attrib['rating']
            measurement_rating_name = measurement.attrib['rating_name']
            measurement_index = measurement.attrib['index']
            
            row = [region_name, station_name, measurement_item, measurement_rating,\
            measurement_rating_name, measurement_index]
            
            rows.append(row)
            
# write results to .csv file
with open('Air-quality-qld.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)    
    
    fieldnames = ['Region', 'Station', 'Measurement Item', 'Measurement Rating',\
    'Measurement Rating Name', 'Measurement Index']
    writer.writerow(fieldnames)
    
    for row in rows:
        writer.writerow(row)
