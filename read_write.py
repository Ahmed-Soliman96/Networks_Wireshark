def write(filename,packets,app=False):
    wrpcap(filename,packets, append=app)
    return None


def read(pcap_file_path):
    packets = rdpcap(pcap_file_path)
    return packets


