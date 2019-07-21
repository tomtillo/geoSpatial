# Anything to do with geospacial data , maps and coordinates

Some useful scripts when working with maps : 


## 1. getxy_from_long_lat.py

Script to convert latitude , longitude combination to x, y coordinates ( Cartesian ) - mostly used in maps - googlemaps,openstreetmaps etc

Explanation : 
Some of the open maps that you find ( google / openstreetmaps ) come in different formats making it difficult to convert and extract the images .

for eg : https://www.openstreetmap.org/#map=16/-37.7932/144.9551

The above URL is of the format 
**domain/zoom/lat/long**
where 

16 = **zoom level** ,  -37.7932 = **latitude** ,  144.9551 = **longitude**

The script can be used to convert the format into x-y cartesian coordinate systems which can be directly used in your script to pull the images.

## Usage : 
`lat2,lng2 = -37.9924558,145.201797`
`print(getXY(lat,lng,zoom))`
