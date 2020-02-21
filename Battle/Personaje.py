class Personaje(object):

    def __init__(self, nombreP, hp, mana, dmg):
        self.nombreP = nombreP
        self.hp = hp
        self.mana = mana
        self.dmg = dmg
        self.lTecnicas = []

    def setTecnicas(self,nuevaTecnicas1, nuevaTecnicas2, nuevaTecnicas3, nuevaTecnicas4):
        self.lTecnicas.append(nuevaTecnicas1)
        self.lTecnicas.append(nuevaTecnicas2)
        self.lTecnicas.append(nuevaTecnicas3)
        self.lTecnicas.append(nuevaTecnicas4)

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

