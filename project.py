from scapy.all import *
from scapy.sendrecv import *
import threading_fun

pkts = []

"""When clicking start bottun to sniff packets"""
def sniff_packets(pktscount = 0, interface = None, pktsfilter = None):
    global pkts
    pkts = sniff(count=pktscount,iface=interface, filter=pktsfilter)

def get_hexa(pkt, rtrn=True):
    return hexdump(pkt, dump=rtrn)

def get_packet_summary(pkt):
    plist.summary(pkt)

def filter_packets(pkt, filter):
    return scapy.plist.filter(pkt, filter)

def save_file(filename, pkts, app=False):
    wrpcap("temp.pcap", pkts, append=app)


"""Executing functions"""
#t = threading_fun.my_thread()

#We would like to pass the "sniff" function to the thread
sniff_packets(pktscount=15)             #Assume sniffing 15 packets only
print(get_hexa(pkts[1]))