from scapy.all import *
from scapy.sendrecv import *
import threading_fun

pkts = []
pktstosave = []
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
def sniff_packets(pktscount = 0, interface = None, pktsfilter = None): #conf.iface == connected interface
    global pkts
    pkts = sniff(count = pktscount,iface = interface, filter = pktsfilter)
    pktstosave.append(pkts)
    #We will make it returns(or prints) the packets to their window inside this function
    print(get_info(pkts[0]))

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
    return (pkt._show_or_dump(dump=True))

"""What to be viewed in the GUI of WireShark packets' list"""
def get_info(pkt):
    pkttime = pkt.time
    if(pkt.haslayer(IP)):
        pkttype = 'IP'
        pktsource = pkt[IP].src
        pktdestination = pkt[IP].dst
    elif(pkt.haslayer(Ether)):
        pkttype = 'Ether'
        pktsource = pkt[Ether].src
        pktdestination = pkt[Ether].dst
    elif(pkt.haslayer(TCP)):
        pkt_type = 'TCP'
        pktsource = pkt[TCP].sport
        pktdestination = pkt[TCP].dport
    pktinfo = pkt.summary()
    # pktsource = pkt[IP].src
    # pktdestination = pkt[IP].dst
    # pktprotocol = pkt[IP].proto
    return [pkttime,pktsource,pktdestination,pkttype,pktinfo]

"""Creates a dectionary of what to be viewed in the GUI of Wireshark packets' list"""
def make_packetslist(pkts):
    global pktslst
    for count in range(len(pkts)):
        pktslst[str(count+1)] = [str(count+1)]+get_info(pkts[count])
    return pktslst

"""To save a '.pcap' file of the packets"""
def save_file(flname, pkts, app=False):
    wrpcap(filename=flname, pkt=pkts, append=app)



"""LET'S START OUR FUNCTIONS"""
#sniffing_thread = threading_fun.my_thread()

#If start sniffing button is clicked
#Try to run in an independent thread, Assume 10 packets and no filters as example. It works
"""
def start():
    sniffing_thread.run(sniff_packets,[1,conf.iface,None])

#Still doesn't work id infinte sniffing
####################################
#start()
pkts = sniff(5,conf.iface,None)
#If stop sniffing button is clicked
def stop():
    sniffing_thread.stop()
####################################
#display_packetdata(pkts[1])
#If a packet is clicked on, get it's no.'i' and display its data and hexa-value
def pkg_data():
    display_packetdata(pkts[i])
    get_hexa(pkt[i])
####################################
#If a filter is set:
def pkg_filter():
    pkts IS Empty -> sniffing_thread.run(sniff_packets,[10,conf.iface,filter])
    pkts IS NOT Empty -> show only pkts.values()[3] == filter $$ Please make sure of this condition
####################################
"""
#If save button is clicked
def save(tosave):
    save_file("mypackets.pcap", tosave)
####################################