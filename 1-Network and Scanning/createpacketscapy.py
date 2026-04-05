from scapy.all import IP, TCP, send

# Step 1: Creating a simple IP packet
packet = IP(dst="192.168.155.66")  # Setting the destination IP
print(packet.show())  # Display packet details

# Step 2: Adding a TCP layer to the IP packet
packet = IP(dst="192.168.155.66") / TCP(dport=80, sport=12345, flags="S")
print(packet.show())

# Step 3: Sending the packet
send(packet)
