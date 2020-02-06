import Personaje
import Tecnicas
import time

class Batalla:

    def menuEligePersonaje(self):
        print("Elige un personje")
        print("[1] El shico voley")
        print("HP: Mana:")
        print("[2] KaanaDiense")
        print("HP: Mana:")
        print("[3] Thor-cido")
        print("HP: Mana:")
        print("[4] ElJefe de PUBG")
        print("HP: Mana:")
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



