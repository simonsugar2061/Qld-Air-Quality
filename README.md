# Qld-Air-Quality
This project visualises air quality index in Queensland using Python and Tableau

## Source data

The source data, which is stored in XML format, is obtained from Queensland Government data website ([source page] (https://data.qld.gov.au/dataset/air-quality-monitoring-live-data-feed)). The XML file containing the source data is also available here.

## Parsing source data

Python is used to parse the source data in the XML file and store the parsed data into a CSV file, which can be directly used by Tableau later. The steps are as follows.

1. The XML file is loaded using the ElementTree package

    ``` python
    tree = ET.ElementTree(file='Air quality - Queensland.xml')
    root = tree.getroot()
    ```

2. The Region tag in the XML file is extracted.

  ``` python
  # Select region tag
  regions = root[0]
  for region in regions:
    print(region.tag, region.attrib['name'])
  ```

3. The information of measurements for each station and region is extracted.

  ``` python
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
  ```

4. Write the extracted information into a CSV file.

  ``` python
  # write results to .csv file
  with open('Air-quality-qld.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)    
    
    fieldnames = ['Region', 'Station', 'Measurement Item', 'Measurement Rating',\
    'Measurement Rating Name', 'Measurement Index']
    writer.writerow(fieldnames)
    
    for row in rows:
        writer.writerow(row)
  ```
  
## Visualisation

The CSV file is then imported to Tableau Public for visualisation. The published dashboard can be found [here] (https://public.tableau.com/profile/simon.su#!/vizhome/QldAirQuality/QueenslandAirQualityIndexAQI).


