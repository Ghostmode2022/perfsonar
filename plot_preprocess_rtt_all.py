#!/usr/bin/python

import numpy as np
import sys
import matplotlib.pyplot as plt
import time
from datetime import datetime
import re
from shutil import copyfile

#open the consolidated file
fileNameI = '/home/sid/perfsonar/description/perfsonar_ip.txt'
fileI = open(fileNameI, 'r')
ip_all = fileI.readlines()

#open the output file
fileNameO = '/home/sid/perfsonar/data/rtt_plot.txt'
fileO = open(fileNameO, 'r+')

for i in range (0, len(ip_all)):
  ip_al1 = ip_all[i]
  ip_al = ip_al1.rstrip("\n")
  fileNameI1 = '/home/sid/perfsonar/data/'+ip_al+'/'+ip_al+'-packet-trace-mean-plot-consolidated'+'.txt'
#               '/home/sid/perfsonar/data/206.207.50.6\n206.207.50.6\n-packet-trace-mean-consolidated.txt'
  fileI1 = open(fileNameI1, 'r')
  ip = fileI1.readlines()
  for item in ip:
    fileO.write("%s" % item)
fileO.close()
with open("/home/sid/perfsonar/data/rtt_plot.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != "Distance	RTT\n":
            f.write(i)
    f.truncate()
