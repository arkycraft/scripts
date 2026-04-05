#! /usr/bin/python

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
from scapy.utils import RandShort
from scapy.layers.l3 import IP
from scapy.layers.l4 import TCP, ICMP
from scapy.sendrecv import sr1

dst_ip = "192.168.52.101"            #Ubuntu 24 VM 

src_port = RandShort()

dst_port=80

ack_flag_scan_resp = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="A"),timeout=10)

if (str(type(ack_flag_scan_resp))=="<type 'NoneType'>"):
	print("Stateful firewall present (Filtered)")

elif(ack_flag_scan_resp.haslayer(TCP)):
	if(ack_flag_scan_resp.getlayer(TCP).flags == 0x4):
		print("No firewall (Unfiltered)")

elif(ack_flag_scan_resp.haslayer(ICMP)):
	if(int(ack_flag_scan_resp.getlayer(ICMP).type)==3 and int(ack_flag_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
		print("Stateful firewall present (Filtered)")