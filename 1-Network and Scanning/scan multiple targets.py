# scan multiple targets

import nmap

scanner = nmap.PortScanner()
targets = ['192.168.52.74', '192.168.52.79', '192.168.52.84']

for ip in targets:
    scanner.scan(ip, '1-65536')
    print(f"\nScan for {ip}:")
    for proto in scanner[ip].all_protocols():
        for port in scanner[ip][proto]:
            state = scanner[ip][proto][port]['state']
            print(f"  {port}/{proto} - {state}")
