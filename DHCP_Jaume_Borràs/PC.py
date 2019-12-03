import ipaddress
from DHCP import DHCP

class PC(object):
    
    def __init__(self, nombre, ip, network, gateway):
        self.nombre = nombre
        self.ip = ip
        self.network = network
        self.gateway = gateway

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre=nombre
    
    def getIp(self):
        return self.ip

    def setIp(self, ip):
        self.ip=ip

    def setNetwork(self, network):
        self.network=network

    def getNetwork(self):
        return self.network

    def setGateway(self, gateway):
        self.gateway=gateway

    def getGateway(self):
        return self.gateway

    def __str__(self):
        info = "Nombre: "+str(self.nombre)+" ip: "+str(self.ip)+" network: "+str(self.network)
        return info

         






