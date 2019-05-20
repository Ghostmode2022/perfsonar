#!/usr/bin/python
# load text
import re
import sys
import time
from subprocess import Popen
import geocoder
import geoip2.database
import geoip2.webservice
from geoip import geolite2
from math import sin, cos, sqrt, atan2, radians
import os

#Defining the value of radian
R = 6373.0

source = sys.argv[1]

#need to convert the ip address into radians 
reader = geoip2.database.Reader('/home/sid/perfsonar/description/GeoLite2-City.mmdb')
response = reader.city(source)
source_lat1 = response.location.latitude
source_long1 = response.location.longitude
source_lat = radians(float(source_lat1))
source_long = radians(float(source_long1))

#get the list of metadata from the output file and store in an array
fileNameM = '/home/sid/perfsonar/data/'+sys.argv[1]+'/'+sys.argv[1]+'-'+'output.txt'
fileM = open(fileNameM, 'r')
textM = []
textM = fileM.read()
with open(fileNameM) as fileM:
    textM = fileM.readlines()
for x in range (0, len(textM)-1):
  metadata = (textM[x])[:-1]

#  print metadata
  fileNameI = '/home/sid/perfsonar/data/'+sys.argv[1]+'/packet-traces/'+sys.argv[1]+'-'+metadata+'-packet-trace'+'.txt'
  fileNameO = '/home/sid/perfsonar/data/'+sys.argv[1]+'/plot/packet-traces/'+sys.argv[1]+'-'+metadata+'-packet-trace'+'.txt'

  fileI = open(fileNameI, 'r')
  fileO = open(fileNameO, 'w')

  textI = []
  textI = fileI.read()
  
  count = textI.count("ts")
#split the data and store in an array with the occurrence of url
#splitarr = textI.rsplit('ts', count)
  splitarr = textI.split('ts')

#get the data between "134.197.11.250/esmond/perfsonar/archive/" and "/","metadata-key":""
  for x in range (1, count+1):
    result = re.search('":(.*),"val":', splitarr[x])
    fileO.write(result.group(1))
    fileO.write("\t")

#convert the unix timestamp into human readable format
    date = time.ctime(int(result.group(1)))
    fileO.write(date)
    fileO.write("\t")

#write the source ip address in the file 
    fileO.write(source)
    fileO.write("\t")

#write the destination ip address in the file 
    result1 = re.search('"ip":"(.*)","', splitarr[x])
    destination = result1.group(1).split('"')[0]
    fileO.write(destination)
    fileO.write("\t")

#get the latitude and longitude of the destination ip address
    response = reader.city(destination)
    dest_lat1 = response.location.latitude
    dest_long1 = response.location.longitude

    dest_lat = radians(dest_lat1)
    dest_long = radians(dest_long1)
  
#get the distance between source and destination
    lat_diff = dest_lat - source_lat
    long_diff = dest_long - source_long
    a = sin(lat_diff / 2)**2 + cos(source_lat) * cos(dest_lat) * sin(long_diff / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    fileO.write(str(distance) + " km")
    fileO.write("\t")

#for x in range (1, count+1):  
    result2 = re.search('"rtt":(.*),"', splitarr[x])
    fileO.write(result2.group(1).split(',')[0])
    fileO.write("\n")


  fileI.close()
  fileO.close()

fileM.close()

#consolidate the data into one text file 
text = []
fileNameOF = '/home/sid/perfsonar/data/'+sys.argv[1]+'/plot/packet-traces/'+sys.argv[1]+'-packet-trace-consolidated'+'.txt'
fileOF = open(fileNameOF, 'w')
fileOF.write("Time_Stamp	Readable_Time	Source	Destination	Distance	RTT")
fileOF.write("\n")

for x in range (0, len(textM)-1):
  metadata = (textM[x])[:-1]
  fileNameIF = '/home/sid/perfsonar/data/'+sys.argv[1]+'/plot/packet-traces/'+sys.argv[1]+'-'+metadata+'-packet-trace'+'.txt'
  fileIF = open(fileNameIF, 'r')  
  textF = fileIF.read()
  fileOF.write(textF)
  fileOF.write("\n")
fileOF.close()
