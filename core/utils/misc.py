import time
import os
def disable_ipv6():
    time.sleep(1)
    os.system('sysctl -w net.ipv6.conf.all.disable_ipv6=1')
    os.system('sysctl -w net.ipv6.conf.default.disable_ipv6=1')
