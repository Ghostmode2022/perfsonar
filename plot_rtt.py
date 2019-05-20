#!/usr/bin/python

import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

#read file to get the values of x and y
data = pd.read_csv("/home/sid/perfsonar/data/rtt_plot.txt", sep="\t")
rtt_all = pd.DataFrame(data)
x = rtt_all.ix[:,0]
y = rtt_all.ix[:,1] 

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("RTT vs Distance between end-points")    
ax1.set_xlabel('Distance')
ax1.set_ylabel('RTT')
ax1.plot(x,y, 'ro', label= 'Relation')
#first argument is the lowest value, second argument is the max value and 
plt.xticks(np.arange(0, 50, 10))
plt.yticks(np.arange(0, 50, 10))
leg = ax1.legend()
plt.show()
#plt.savefig('/home/sid/perfsonar/data/rtt__dist_plot.png')
