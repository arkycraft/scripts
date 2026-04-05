import pyshark

capture = pyshark.LiveCapture(interface="wlan0")
capture.sniff(timeout=10)
for packet in capture.sniff_continuously(packet_count=5):
    print(packet)
    