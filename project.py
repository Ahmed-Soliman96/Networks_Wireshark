from scapy.all import *
from scapy.sendrecv import *

intfces = {}
#List of interface to choose which one to sniff from
def get_interfaces():
    global intfces
    lst = get_windows_if_list()
    for i in range(len(lst)):
        intfces[i] = get_windows_if_list()[i]['name']
    return intfces


#When you single click on a packet its data should be viewed
def get_hexa(pkt):
    return hexdump(pkt, dump=True)

#When you double click on a packet its data should be viewed
def display_packetdata(pkt):
    return pkt._show_or_dump(dump= True)

"""What to be viewed in the GUI of WireShark packets' list"""
def get_info(pkt):
    pkttime = pkt.time
    if(pkt.haslayer(IP)):
        pktsource = pkt[IP].src
        pktdestination = pkt[IP].dst
    elif(pkt.haslayer(Ether)):
        pktsource = pkt[Ether].src
        pktdestination = pkt[Ether].dst
    """
    elif(pkt.haslayer(TCP)):
        pktsource = pkt[TCP].sport
        pktdestination = pkt[TCP].dport
    """
    pktinfo = pkt.summary()
    typ = pktinfo.split(' / ')
    if len(typ) > 3:
        if  (((typ[2]).split(' ')[0] == 'TCP') or ((typ[2]).split(' ')[0] == 'UDP')) and ((typ[3]).split(' ')[0] != 'DNS'):
            pkttype = (typ[2]).split(' ')[0]
        elif ((typ[2]).split(' ')[0][:4] == 'ICMP'):
            pkttype = 'ICMP'
        else:
            pkttype = (typ[3]).split(' ')[0]
    elif len(typ) == 3:
        if (typ[1])[0].isnumeric():
            pkttype = 'TCP'
        elif ((typ[2]).split(' ')[0] == 'TCP') or ((typ[2]).split(' ')[0] == 'UDP') or ((typ[2]).split(' ')[0] == 'ARP'):
            pkttype = (typ[2]).split(' ')[0]
        else:
            pkttype = (typ[1]).split(' ')[0]
    else:
        pkttype = (typ[1]).split(' ')[0]

    return [pkttime,pktsource,pktdestination,pkttype,pktinfo]

#Creates a dectionary of what to be viewed in the GUI of Wireshark packets' list
def make_packetslist(pkts):
    global pktslst
    for count in range(len(pkts)):
        pktslst[str(count+1)] = [str(count+1)]+get_info(pkts[count])
    return pktslst

#If save button is clicked
def save(tosave, app=False):
    wrpcap(filename="mypackets.pcap", pkt=tosave, append=app)