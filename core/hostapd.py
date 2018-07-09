import os
import sys
import ctypes
import threading
import time
import settings.paths

HOSTAPD_EXEC_PATH = 'hostapd-eaphammer/hostapd/hostapd-eaphammer'
HOSTAPD_LIB_PATH = 'hostapd-eaphammer/hostapd/libhostapd-eaphammer.so'

class Hostapd(object):

    def __init__(self, conf_path, debug=False):

        self.exec_path = HOSTAPD_EXEC_PATH
        self.debug = debug 
        self.lib_path = HOSTAPD_LIB_PATH
        
        self.conf_path = conf_path
        self.sleep_time = 4

    def start(self):

        with open(self.conf_path, 'a') as fd:
            fd.write('eap_user_file=%s\n' % settings.paths.EAP_USER_FILE)
            fd.write('ca_cert=%s\n' % settings.paths.CA_PEM)
            fd.write('server_cert=%s\n' % settings.paths.SERVER_PEM)
            fd.write('private_key=%s\n' % settings.paths.PRIVATE_KEY)
            fd.write('dh_file=%s\n' % settings.paths.DH_FILE)

        argv = [
            self.exec_path,
            '-N',
        ]
        if self.debug:
            argv.append('-d')
        argv.append(self.conf_path)
    
        argc = len(argv)
        argv_mem = ctypes.c_char_p * argc
        argv = argv_mem(*argv)

        self.libhostapd = ctypes.cdll.LoadLibrary(self.lib_path)

        try:

            self.thread = threading.Thread(target=self.libhostapd.main, args=(argc, argv))
            self.thread.start()

            print
            print '[hostapd] AP starting...'
            print
            time.sleep(self.sleep_time)

        except KeyboardInterrupt:
            
            self.stop()

    def stop(self):


        print '[hostapd] Terminating event loop...'
        self.libhostapd.eloop_terminate()

        print '[hostapd] Event loop terminated.'
        
        if self.thread.is_alive():
        
            print '[hostapd] Hostapd worker still running... waiting for it to join.'
            print
            self.thread.join(5)
            print
            print '[hostapd] Worker joined.'

        print '[hostapd] AP disabled.'
        print
