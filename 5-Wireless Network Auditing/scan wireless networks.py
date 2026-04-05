import pyshark
# Capture wireless packets on the specified interface
capture = pyshark.LiveCapture(interface='wlan0', display_filter='wlan.fc.type_subtype == 0x08')
# Loop through captured packets and print SSID and BSSID
print('[!] Scanning for wireless networks...')
for packet in capture.sniff_continuously():
    try:
        ssid = packet.wlan_mgt.ssid
        bssid = packet.wlan.bssid
        print(f"[+] Found Network: SSID: {ssid}, BSSID: {bssid}")
    except AttributeError:
        # Skip packets that don't have the required fields
        continue