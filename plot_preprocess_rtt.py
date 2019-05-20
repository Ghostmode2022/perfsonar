#!/usr/bin/python
#python plot_throughput.py 206.207.50.6 throughput ae7b607a924f4af8b3f8f979c70f95f1 

#First argument is the ip address
#Second argument is the event-type
#Third argument is the metadata

import numpy as np
import sys
import matplotlib.pyplot as plt
import time
from datetime import datetime
import pandas as pd
import re
from shutil import copyfile

#open the consolidated file
fileNameI = '/home/sid/perfsonar/data/'+sys.argv[1]+'/plot/packet-traces/'+sys.argv[1]+'-packet-trace-consolidated'+'.txt'
fileI = open(fileNameI, 'r')

fileNameO = '/home/sid/perfsonar/data/'+sys.argv[1]+'/plot/packet-traces/'+sys.argv[1]+'-packet-trace-mean-plot-consolidated'+'.txt'
fileO = open(fileNameO, 'w')

fileNameC = '/home/sid/perfsonar/data/'+sys.argv[1]+'/'+sys.argv[1]+'-packet-trace-mean-plot-consolidated'+'.txt'

#load data in pandas array
rtt_all1 = pd.read_csv(fileI, sep="\t")
rtt_all = pd.DataFrame(rtt_all1) 

#deleting all the rows which does not contain any value
#rtt_all = rtt_all1.dropna(axis=0, how='all')

#getting all the unique values in destination
dest_list = rtt_all.Destination.unique()

dest_list_mean = []

fileO.write("Distance	RTT")
fileO.write("\n")

for i in range (0, len(dest_list)):

#create a new numpy array to store all the values belonging to any parti
  dest_list_particular = []

#assigning data to the array
  dest_list_particular = rtt_all.loc[rtt_all['Destination'] == dest_list[i], 'RTT']

#writing the distance between the source and the destination
  distance = rtt_all.loc[rtt_all['Destination'] == dest_list[i], 'Distance']
  dist1 = str(distance.unique())

#need to get only the distance without the km
  dist2 = dist1[:-5]
  dist = dist2[2:]

#writing the distance in the file
  fileO.write(dist)
  fileO.write("\t")

#writing the mean value of the rtt
  mean_rtt1 = np.mean(dest_list_particular)

#converting the mean rtt to be 3 places after decimal
  mean_rtt = np.around(mean_rtt1, decimals=3)

#  print(mean_rtt)
  fileO.write(str(mean_rtt))
  fileO.write("\n")
fileO.close()
fileI.close()
copyfile(fileNameO, fileNameC)

'''#textI = []
textI = fileI.read()
# Replace the target string
textO1 = textI.replace(',"val":', '	')
textO2 = textO1.replace('{"ts":', '')
textO3 = textO2.replace('[', '')
textO4 = textO3.replace(']', '')
textO5 = textO4.replace('},', "\n")
textO = textO5.replace('}', '')
textO = textO.split('\n')

x = [row.split('	')[0] for row in textO]
for i in range (len(x)):
  a = x[i]
  b = int(a)
  c = datetime.utcfromtimestamp(b).strftime("%m:%d:%Y-%H:%M:%S")
  x[i] = c
y = [row.split('	')[1] for row in textO]

fig = plt.figure()

ax1 = fig.add_subplot(111)



ax1.set_title("Throughput timeseries graph")    
ax1.set_xlabel('time-stamp')
ax1.set_ylabel('throughput')
#c='r',
ax1.plot(x,y, 'ro', label= sys.argv[3])

#first argument is the lowest value, second argument is the max value and 
plt.xticks(np.arange(0, 50, 10))
plt.yticks(np.arange(0, 50, 10))

#ax1.pyplot.locator_params(axis='y', nbins=6)
#ax1.pyplot.locator_params(axis='x', nbins=10)



leg = ax1.legend()

plt.show()'''
