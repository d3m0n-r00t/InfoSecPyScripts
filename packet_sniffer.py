import scapy.all as scapy
from scapy.layers import http


def snif(interface):
    scapy.sniff(iface = interface,store = False, prn = process_packets)
    


def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
         print(packet)
    

snif('wlp3s0')