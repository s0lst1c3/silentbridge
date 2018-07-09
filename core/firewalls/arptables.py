import os

def drop_all():
    os.system('arptables -A OUTPUT -j DROP')

def allow_all():
    os.system('arptables -D OUTPUT -j DROP')

def flush():
    os.system('arptables -F')

def default_accept():
    os.system('arptables -P INPUT ACCEPT')
    os.system('arptables -P OUTPUT ACCEPT')
    os.system('arptables -P FORWARD ACCEPT')

def allow_outbound(iface):
    os.system('arptables -A OUTPUT -o %s -j ACCEPT' % iface)
