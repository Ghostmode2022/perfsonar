#!/usr/bin/python
# load text
import re
import sys
import sys, os
import subprocess
print "This is the name of the script: ", sys.argv[1]
var = sys.argv[1]
fileNameI = '/home/sid/perfsonar/data/'+sys.argv[1]+'/'+sys.argv[1]+'.txt'
fileNameO = '/home/sid/perfsonar/data/'+sys.argv[1]+'/'+sys.argv[1]+'-output.txt'
fileI = open(fileNameI, 'r')
fileO = open(fileNameO, 'w')
textI = []
textI = fileI.read()

#count the number times the word "url" appears
count = textI.count("url")
print 'The number of occurrence of url %s' %count

#split the data and store in an array with the occurrence of url
splitarr = textI.rsplit('url', count)

#get the data between "134.197.11.250/esmond/perfsonar/archive/" and "/","metadata-key":""
for x in range (1, count+1):
  pre = sys.argv[1]+'/esmond/perfsonar/archive/'
  post = '/","metadata-key":"'
  start = splitarr[x].index( pre ) + len( pre )
  end = splitarr[x].index( post, start )
  fileO.write(splitarr[x][start:end])
  fileO.write("\n")

#create as many variable as many as the metadata
  globals()['metadata%s' % x] = splitarr[x][start:end]
#Need to un-comment to see the output
#  print (eval("metadata%s" % (x)))

fileI.close()
fileO.close()
cmd = "./perf_get_throughput.sh "+var
#call the shell script with the argument provided in the previous file to be sent as argument in this step as well.
#os.system(cmd)
