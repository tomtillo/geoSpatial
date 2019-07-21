
import urllib.request
from PIL import Image
import os
import math
import urllib as urllibObj
import urllib # this is for image retrieval
from urllib.request import Request, urlopen # this is for soup
import sys
import time 

def getXY(lat,lng,zoom):

        tile_size = 256
        # Use a left shift to get the power of 2
        # i.e. a zoom level of 2 will have 2^2 = 4 tiles
        numTiles = 1 <<  zoom
        # Find the x_point given the longitude
        point_x = (tile_size / 2 + lng * tile_size / 360.0) * numTiles // tile_size
        # Convert the latitude to radians and take the sine
        sin_y = math.sin(lat * (math.pi / 180.0))
        # Calulate the y coorindate
        point_y = ((tile_size / 2) + 0.5 * math.log((1 + sin_y) / (1 - sin_y)) * -(
        tile_size / (2 * math.pi))) * numTiles // tile_size
        #print("x = %d y= %d" %(int(point_x), int(point_y)))
        return int(point_x), int(point_y)

zoom = 20
lat,lng = -37.9821368,145.186968
lat2,lng2 = -37.9924558,145.201797
print(getXY(lat,lng,zoom))
print(getXY(lat2,lng2,zoom))