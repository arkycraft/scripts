# Simple Port Scan

import nmap
scanner = nmap.PortScanner()

ip = '192.168.52.120'  # Replace with your target IP
scanner.scan(ip, '20-1024')  # Scans ports 20 to 1024

print(f"Results for {ip}")
for proto in scanner[ip].all_protocols():
    ports = scanner[ip][proto].keys()
    for port in ports:
        state = scanner[ip][proto][port]['state']
        print(f"Port {port}/{proto}: {state}")
