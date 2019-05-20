#!/bin/bash
ip="$1"
fileI="/home/sid/perfsonar/data/$1/$1-output.txt" #need to include the data directory

mkdir /home/sid/perfsonar/data/$ip/packet-traces

while IFS= read -r metadata
do
  #Querying Packet Traces
  touch /home/sid/perfsonar/data/$ip/packet-traces/$ip-packet-trace.txt  
  curl "http://$ip/esmond/perfsonar/archive/$metadata/packet-trace/base?time-range=604800" >> /home/sid/perfsonar/data/$ip/packet-traces/$ip-$metadata-packet-trace.txt
done < "$fileI"
#146.83.90.6	7aa7ec06986b462abe5df054cd48e278	packet-trace

#curl http://146.83.90.6/esmond/perfsonar/archive/7aa7ec06986b462abe5df054cd48e278/packet-trace/base?time-range=604800

##curl "http://archive.example.net/esmond/perfsonar/archive/?event-type=throughput"
##curl http://archive.example.net/esmond/perfsonar/archive/641860b2004c46a7b21fe26e5ffea9af/packet-trace/base?time-range=600
##curl "http://archive.example.net/esmond/perfsonar/archive/?source=10.1.1.1&destination=10.1.1.2"
