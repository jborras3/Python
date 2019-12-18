import ipaddress
from PC import PC
from DHCP import DHCP
from switch import switch

class router(object):

    def __init__(self):
        self.switches = []

    def getSwitches(self):
        return self.switches

    def AddSwitch(self, switch):
        self.switches.append(switch)
