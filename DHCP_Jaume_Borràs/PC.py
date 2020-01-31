import ipaddress
from DHCP import DHCP
from so import so

class PC(object):
    
    def __init__(self, nombre, ip, network, gateway,hddSpace, so):
        self.nombre = nombre
        self.ip = ip
        self.network = network
        self.gateway = gateway
        self.hddSpace = hddSpace
        self.so = so


    def getHddSpace(self):
        return self.hddSpace

    def getSo(self):
        return self.so

    def setHddSpace(self, hddSpace):
        self.hddSpace=hddSpace

    def setSo(self, so):
        self.so=so

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

    def IntallSO(self, ):

     def __str__(self):
        info = "Nombre: "+str(self.nombre)+" so: "+so.getName()+so.getVersion()+" "+so.getArchitecture()+"Espacio de disco "+str(self.hddSpace)+"MB"+" ip: "+str(self.ip)+" network: "+str(self.network)
        return info