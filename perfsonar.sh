#!/bin/bash
ip=$1
#creating directory
echo -e "\n Creating the directory specific to this ip \n" 
mkdir /home/sid/perfsonar/data/$ip
#files and folder creation for plotting putpose for only the packet-traces event type where we can find rtt
mkdir /home/sid/perfsonar/data/$ip/plot
mkdir /home/sid/perfsonar/data/$ip/plot/packet-traces
touch /home/sid/perfsonar/data/$ip/plot/packet-traces/$ip-plot.txt
#executing curl query
echo -e "\n Executing the first curl query to get the metadata value \n"
curl http://$ip/esmond/perfsonar/archive/ >> /home/sid/perfsonar/data/$ip/$ip.txt
#creating the output file to store the metadata (touch command is used to create a file without any content)
echo -e "\n Create the output file\n"
touch /home/sid/perfsonar/data/$ip/$ip-output.txt
#calling the python script for extracting the metadata
echo -e "\n Executing the python file to extract the alphaneumeric value \n"
chmod 777 preprocess.py
./preprocess.py $ip
