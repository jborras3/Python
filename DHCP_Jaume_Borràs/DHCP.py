import ipaddress


class DHCP(object):

    def __init__(self, ipStaticDHCP, ipInicioRango, NumPCRango, network, gateway):
        self.ipStaticDHCP = ipStaticDHCP
        self.ipInicioRango = ipInicioRango
        self.NumPCRango = NumPCRango
        self.network = network
        self.ipDisponibles = []
        self.gateway = gateway

    def setipStaticDHCP(self, ipStaticDHCP):
        self.ipStaticDHCP = ipStaticDHCP

    def setipInicioRango(self, ipInicioRango):
        self.ipInicioRango = ipInicioRango

    def setNumPCRango(self, NumPCRango):
        self.NumPCRango = NumPCRango

    def setnetwork(self, network):
        self.network = network

    def getnetwork(self):
        return self.network

    def getipStaticDHCP(self):
        return self.ipStaticDHCP

    def getipInicioRango(self):
        return self.ipInicioRango

    def getNumPCRango(self):
        return self.NumPCRango

    def getipDisponibles(self):
        return self.ipDisponibles

    def anadirDisponibles(self, ipAInsertar):
        self.ipDisponibles.append(ipAInsertar)

    def setGateway(self, gateway):
        self.gateway=gateway

    def getGateway(self):
        return self.gateway