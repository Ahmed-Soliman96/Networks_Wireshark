from scapy.all import *
from scapy.sendrecv import *
import threading_fun

pkts = []
pktslst = {}
intfces = {}

"""List of interface to choose which one to sniff from"""
def get_interfaces():
    global intfces
    lst = get_windows_if_list()
    for i in range(len(lst)):
        intfces[str(i+1)] = get_windows_if_list()[i]['name']
    return intfces

"""INTO THREAD"""
"""When clicking start bottun to sniff packets ||| Also can be used for filtering packets by setting the 'pktsfilter' as we want"""
def sniff_packets(pktscount = 0, interface = conf.iface, pktsfilter = None): #conf.iface == connected interface
    global pkts
    pkts = sniff(count = pktscount,iface = interface, filter = pktsfilter)
    return pkts
"""OUT OF THREAD"""

"""When choosing a specific filter for shown packets
def filter_packets(fltr):
     global pkts
     pkts = sniff_packets(pktsfilter = fltr)
     return pkts
"""

"""When you single click on a packet its data should be viewed"""
def get_hexa(pkt):
    return hexdump(pkt, dump=True)

"""When you double click on a packet its data should be viewed"""
def display_packetdata(pkt):
    pkt.display()

"""What to be viewed in the GUI of Wireshark packets' list"""
def get_info(pkt):
    pkttime = pkt.time
    pktsource = pkt[IP].src
    pktdestination = pkt[IP].dst
    pktprotocol = pkt[IP].proto
    pktinfo = pkt.summary()
    return [pkttime,pktsource,pktdestination,pktprotocol,pktinfo]

"""Creates a dectionary of what to be viewed in the GUI of Wireshark packets' list"""
def make_packetslist(pkts):
    global pktslst
    for count in range(len(pkts)):
        pktslst[str(count+1)] = [str(count+1)]+get_info(pkts[count])
    return pktslst

"""To save a '.pcap' file of the packets"""
def save_file(flname, pkts, app=False):
    wrpcap(filename=flname, pkt=pkts, append=app)

#####################################
t = threading_fun.my_thread() #Try to run in an independent thread, but still doesn't work
t.run(sniff_packets,[0]) #To be used used on clicking start #Assume 10 packets only and no filters as example, It works
print(make_packetslist(pkts)) #Dectionary to be used in the packets' view window
save_file("mypackets.pcap", pkts)

"""
    for i in range(len(pkts)):
        print(get_hexa(pkts[i]))
        display_packetdata(pkts[i])
"""
#time.sleep(1)