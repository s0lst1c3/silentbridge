import argparse
import time
import state_banners

from nanpy import (ArduinoApi, SerialManager)

class Splitters(object):

    def __init__(self, uc_pin=7, ub_pin=8, pc_pin=12, pb_pin=13):

        # set member variables
        self.upstream_state = None
        self.phy_state = None
        self.uc_pin = uc_pin
        self.ub_pin = ub_pin
        self.pc_pin = pc_pin
        self.pb_pin = pb_pin

        # connect to the arduino device over serial connection
        self.connection = SerialManager()
        self.api = ArduinoApi(connection=self.connection)

        # initialize pins as output
        self.api.pinMode(self.uc_pin, self.api.OUTPUT)
        self.api.pinMode(self.ub_pin, self.api.OUTPUT)
        self.api.pinMode(self.pc_pin, self.api.OUTPUT)
        self.api.pinMode(self.pb_pin, self.api.OUTPUT)

    def print_state(self, pretty=False):

        if self.upstream_state is None or self.phy_state is None:

            print 'State unknown'
        
        else:

            print 'Upstream Connected:', self.upstream_state
            print 'PHY Connected:', self.phy_state
            if pretty:
                if self.upstream_state:
                    print state_banners.upstream_connected
                else:
                    print state_banners.upstream_bypass
                print state_banners.banner_center
                if self.phy_state:
                    print state_banners.phy_connected
                else:
                    print state_banners.phy_bypass

    def set_upstream(self, state):

        if state:
            self._flip_switch(self.uc_pin)
        else:
            self._flip_switch(self.ub_pin)
        self.upstream_state = state

    def set_phy(self, state):

        if state:
            self._flip_switch(self.pc_pin)
        else:
            self._flip_switch(self.pb_pin)
        self.phy_state = state

    def _flip_switch(self, relay_pin):

        self.api.digitalWrite(relay_pin, self.api.HIGH)
        time.sleep(1)
        self.api.digitalWrite(relay_pin, self.api.LOW)

