from Tecnicas import Tecnicas
from Personaje import Personaje
import time

class Batalla:

    def __init__(self):
        self

    def menuEligePersonaje(self):
        print("Elige un personje")
        print("[1] ElJefe de PUBG")
        print("HP: 500 Mana: 120")
        print("[2] KHANTOSO")
        print("HP: 700 Mana: 90")
        print("[3] Er shico voley")
        print("HP: 400 Mana: 250 ")
        print("[4] Thor-cido")
        print("HP: 550 Mana: 111 ")
        time.sleep(0.5)

    def menuCombate(self):
        while False:
            print("Elige acción")
            print("[1] Ataques")
            print("[2] Bolsillo de potis")
            x = input()
            if x == 1:
                Batalla.menuAtaques()
                break
            elif x == 2:
                Batalla.menuPotis()
                break

    def menuAtaques(self):
        print("[1] "+p1.lTecnica()[0].getnombreT())
        print("[2] "+p1.lTecnica()[1].getnombreT())
        print("[3] "+p1.lTecnica()[2].getnombreT())
        print("[4] "+p1.lTecnica()[3].getnombreT())



