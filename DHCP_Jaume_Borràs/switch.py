import ipaddress
from DHCP import DHCP
from PC import PC


class switch(object):

    def __init__(self, ipDisponibles, PCs, network, DHCP):
        self.ipDisponibles = []
        self.PCs = []
        self.network = network
        self.DHCP = DHCP

    def anadirDisponibles(self, ipAInsertar):
        self.ipDisponibles.append(ipAInsertar)

    def setnetwork(self, network):
        self.network = network

    def setDHCP(self, DHCP):
        self.DHCP = DHCP

    def anadirPCs(self, pc):
        self.PCs.append(pc)

    def getipDisponibles(self):
        return self.ipDisponibles

    def getnetwork(self):
        return self.network

    def getPCs(self):
        return self.PCs

    def getDHCP(self):
        return self.DHCP

    def getInfoPcs(self):
        for pc in self.PCs :
            print(pc)