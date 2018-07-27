import os
import time

class Bridge(object):

    def __init__(self, name, mac=None):

        self.name = name
        self.mac = mac

    def create(self):

        os.system('brctl addbr %s' % self.name)
        time.sleep(.5)

    def remove(self):

        os.system('brctl delbr %s' % self.name)
        time.sleep(.5)

    def add_iface(self, iface, mac=None):

        if mac is not None:

            os.system('ifconfig %s down' % iface)
            time.sleep(2)
            os.system('macchanger -m %s %s' % (mac, iface))
            time.sleep(2)

        os.system('brctl addif %s %s' % (self.name, iface))
        time.sleep(.5)

    def del_iface(self, iface):
        os.system('brctl delif %s %s' % (self.name, iface))
        time.sleep(.5)

    def _get_all_ifaces(self):

        return os.listdir('/sys/devices/virtual/net/%s/brif' % self.name)

    def del_all_ifaces(self):

        for iface in self._get_all_ifaces():
            self.del_iface(iface)

    def all_ifaces_up(self):

        for iface in self._get_all_ifaces():
            os.system('ifconfig %s 0.0.0.0 up promisc' % iface)

    def all_ifaces_down(self):

        for iface in self._get_all_ifaces():
            os.system('ifconfig %s down' % iface)

    def up(self, bridge_ip):

        if self.mac is not None:
            os.system('macchanger -m %s %s' % (self.mac, self.name))
            time.sleep(2)
        os.system('ifconfig %s %s up promisc' % (self.name, bridge_ip))

    def down(self):

        os.system('ifconfig %s down' % self.name)

    def enable_8021x_forwarding(self):

        os.system('echo 8 > /sys/class/net/%s/bridge/group_fwd_mask' % self.name) 

    def enable_ip_forwarding(self):

        os.system('echo 1 > /proc/sys/net/ipv4/ip_forward') 
