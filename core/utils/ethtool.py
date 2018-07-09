import os

def reset_link(iface):
    os.system('ethtool -r %s' % iface)
