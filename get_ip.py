#!/usr/bin/python
#pass the filename with the list of ip as command line argument
import re
import sys
import sys, os
from subprocess import Popen
fileNameI = sys.argv[1]
fileI = open(fileNameI, 'r')
textI = []
for line in fileI:
  text = line.split("\t")[3]    
  text1 = text.rstrip()
  textI.append(text1)
num_line = sum(1 for line in open(sys.argv[1]))
for x in range(num_line):
  print textI[x]
  Process=Popen('./perfsonar.sh %s' % (str(textI[x])), shell=True)
fileI.close()
