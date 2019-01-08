import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip)

    # arp packet created
    arp_request = scapy.ARP(pdst = ip)
    # print(arp_request.summary())

    #creating custom ether layer
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") # setting broadcast macaddress 
    # print(broadcast.summary())

    arp_request_broadcast = broadcast/arp_request # new packet,comb of two packets
    # print(arp_request_broadcast.summary())  Ether / ARP who has Net('192.168.43.1/24') says 192.168.43.228
    # arp_request_broadcast.show()

    answered_packets = scapy.srp(arp_request_broadcast,timeout = 1)[0] #sending packet,send and receive packets
    answered_packets.summary()

scan('192.168.43.1/24')