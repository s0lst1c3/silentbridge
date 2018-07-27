import os

def dnat_map_port(bridge_iface, client_ip, ssh_port, bridge_ip):
    os.system('iptables -t nat -A PREROUTING -i %s -d %s -p tcp --dport %d -j DNAT --to %s:22' % (bridge_iface, client_ip, ssh_port, bridge_ip))

def source_nat(bridge_iface, bridge_ip, client_ip):
    os.system('iptables -t nat -A POSTROUTING -o %s -s %s -p tcp -j SNAT --to %s:61000-62000' % (bridge_iface, bridge_ip, client_ip))
    os.system('iptables -t nat -A POSTROUTING -o %s -s %s -p udp -j SNAT --to %s:61000-62000' % (bridge_iface, bridge_ip, client_ip))
    os.system('iptables -t nat -A POSTROUTING -o %s -s %s -p icmp -j SNAT --to %s' % (bridge_iface, bridge_ip, client_ip))

def drop_all():
    os.system('iptables -A OUTPUT -j DROP')

def allow_all():
    os.system('iptables -D OUTPUT -j DROP')

def flush():
    os.system('iptables -F')

def allow_outbound(iface, port=22):
    os.system('iptables -A OUTPUT -o %s -p tcp --dport %d -j ACCEPT' % (iface, port))
    os.system('iptables -I INPUT -i %s -m state --state ESTABLISHED,RELATED -j ACCEPT' % (iface))

def default_accept():
    os.system('iptables -P INPUT ACCEPT')
    os.system('iptables -P OUTPUT ACCEPT')
    os.system('iptables -P FORWARD ACCEPT')
