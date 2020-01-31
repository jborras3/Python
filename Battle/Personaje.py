import Tecnicas
import Batalla


class Personaje(object):

    def __init__(self, nombreP, hp, mana, dmg):
        self.nombreP = nombreP
        self.hp = hp
        self.mana = mana
        self.dmg = dmg
        self.lTecnicas = []

    def setnombreP(self, nombreP):
        self.nombreP = nombreP

    def gethp(self):
        return self.hp

    def sethp(self, hp):
        self.hp = hp

    def getnombreP(self):
        return self.nombreP

    def setmana(self, mana):
        self.mana = mana

    def getmana(self):
        return self.mana

    def setdmg(self, dmg):
        self.dmg = dmg

    def getdmg(self):
        return self.dmg

    def gettecnicas(self):
        for Tecnicas in self.lTecnicas:
            print(Tecnicas)

    def setnuevatecnica(self,Tecnicas):
        self.lTecnicas.append(Tecnicas)