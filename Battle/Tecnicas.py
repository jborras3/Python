import Personaje
import Batalla


class Tecnicas():

    def __init__(self, nuevoNombreT, nuevoCriticoT, nuevoDanoT, nuevoManaT, nuevaPunteria, nuevoEfectoT):
        self.nombreT = nuevoNombreT
        self.criticoT = nuevoCriticoT
        self.danoT = nuevoDanoT
        self.manaT = nuevoManaT
        self.punteria = nuevaPunteria
        self.efectoT = nuevoEfectoT

    def getNombreT(self):
        return self.nombreT

    def setNombreT(self, nuevoNombreT):
        self.nombreT = nuevoNombreT

    def getCriticoT(self):
        return self.criticoT

    def setCriticoT(self, nuevoCriticoT):
        self.criticoT = nuevoCriticoT

    def getDanoT(self):
        return self.danoT

    def setDanoT(self, nuevoDanoT):
        self.danoT = nuevoDanoT

    def getManaT(self):
        return self.manaT

    def setManaT(self, nuevoManaT):
        self.manaT = nuevoManaT

    def getPunteria(self):
        return self.punteria

    def setPunteria(self, nuevaPunteria):
        self.punteria = nuevaPunteria

    def getEfectoT(self):
        return self.efectoT

    def setEfectoT(self, nuevoEfectoT):
        self.efectoT = nuevoEfectoT