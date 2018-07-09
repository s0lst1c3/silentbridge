from scapy.all import *

def force_reauthentication(iface, client_mac):

    # send an EAPOL-Start broadcast from client's mac
    sendp(Ether(src=client_mac, dst="01:80:c2:00:00:03")/EAPOL(type=1), iface=iface)
