from scapy.all import sniff

def packet_callback(packet):
    print(f"\n[+] Packet Captured:")
    if packet.haslayer("IP"):
        print(f"   Source IP: {packet['IP'].src}")
        print(f"   Destination IP: {packet['IP'].dst}")
        print(f"   Protocol: {packet['IP'].proto}")
    if packet.haslayer("Raw"):
        print(f"   Payload Data: {packet['Raw'].load}")

print("Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)