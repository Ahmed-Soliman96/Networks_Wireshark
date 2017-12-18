from scapy.all import *
from scapy.sendrecv import *
import threading_fun

pkts = []
lst = []

"""INTO THREAD"""
"""When clicking start bottun to sniff packets"""
def sniff_packets(pktscount = 0, interface = None, pktsfilter = None):
    global pkts
    pkts = sniff(count = pktscount,iface = interface, filter = pktsfilter)
    return pkts
"""OUT OF THREAD"""

"""When you single click on a packet its data should be viewed"""
def get_hexa(pkt):
    return hexdump(pkt, dump=True)

"""When you double click on a packet its data should be viewed"""
def display_packetdata(pkt):
    pkt.display()
"""When choosing a specific filter for shown packets"""
def filter_packets(pkt, filter):
    return scapy.plist.filter(pkt, filter)

"""What to be viewed in the GUI of Wireshark packets' list"""
def get_info(pkt):
    pkttime = pkt.time
    pktsource = pkt[IP].src
    pktdestination = pkt[IP].dst
    pktprotocol = pkt[IP].proto
    pktinfo = pkt.summary()
    return [pkttime,pktsource,pktdestination,pktprotocol,pktinfo]

"""What to be viewed in the GUI of Wireshark packets' list"""
def make_packetslist(pkt):
    global lst
    lst.append([len(lst)+1]+get_info(pkt))

"""To save a '.pcap' file of the packets"""
def save_file(flname, pkts, app=False):
    wrpcap(filename=flname, pkt=pkts, append=app)
#####################################

sniff_packets(pktscount=2) #Assume 2 packets only as example, It works
for i in range(len(pkts)):
    print(get_info(pkts[i]))
    print(get_hexa(pkts[i]))
    make_packetslist(pkts[i])
print(lst)

save_file("mypackets.pcap",pkts)

#get_packet_summary(pkts[i][0])
#t = threading_fun.my_thread()
#t = threading_fun.my_thread(target = sniff(), args=())
#print(filter_packets(pkts[i],"TCP"))

"""
pkts = scapy.sendrecv.sniff(3)
print(pkts)
print('---------------------------------------')
pkt1 = pkts[0]
scapy.utils.hexdump(pkt1, dump = False)
"""