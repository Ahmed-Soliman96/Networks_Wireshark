from scapy.all import *
from scapy.sendrecv import *
import threading_fun

pkts = []
pktslst = {}

"""INTO THREAD"""
"""When clicking start bottun to sniff packets ||| Also can be used for filtering packets by setting the 'pktsfilter' as we want"""
def sniff_packets(pktscount = 0, interface = None, pktsfilter = None):
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
    #global lst
    #lst.append([len(lst)+1]+get_info(pkt))
    global pktslst
    for count in range(len(pkts)):
        pktslst[str(count+1)] = [str(count+1)]+get_info(pkts[count])
    return pktslst

"""To save a '.pcap' file of the packets"""
def save_file(flname, pkts, app=False):
    wrpcap(filename=flname, pkt=pkts, append=app)
#####################################

def runcode():
    sniff_packets(pktscount=10,pktsfilter="") #To be used used on clicking start #Assume 10 packets only and no filters as example, It works
    save_file("mypackets.pcap", pkts)
    print(make_packetslist(pkts)) #Dectionary to be used in the packets' view window
    """
    for i in range(len(pkts)):
        print(get_hexa(pkts[i]))
        display_packetdata(pkts[i])
    """
t = threading_fun.my_thread(runcode()) #Try to run in an independent thread, but still doesn't work
#t.start()
#time.sleep(1)