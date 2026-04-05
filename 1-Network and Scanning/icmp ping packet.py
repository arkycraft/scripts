from scapy.all import ICMP, IP, send

# Creating an ICMP Echo request packet
icmp_packet = IP(dst="192.168.155.66") / ICMP()
send(icmp_packet)
