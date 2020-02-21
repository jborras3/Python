from Tecnicas import Tecnicas
from Personaje import Personaje
from Batalla import Batalla
import time

print("   ___             _       _        _                    __  __  ")
print("  | _ )   __ _    | |_    | |_     | |     ___     ___  |  \/  |   ___    _ __     ___ ")
print("  | _ \  / _` |   |  _|   |  _|    | |    / -_)   |___| | |\/| |  / -_)  | '  \   / -_) ")
print("  |___/  \__,_|   _\__|   _\__|   _|_|_   \___|   _____ |_|__|_|  \___|  |_|_|_|  \___|  ")
print("_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|     |_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"| ")
print("\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'")
print("                                         Welcome")

m = Batalla()

time.sleep(3.5)

m.menuEligePersonaje()

salir = False

while salir == False:
    slcP = input()
    if slcP == 1:
        p1 = Personaje("ElJefe de PUBG", 400, 120, 20)
        tecnica1 = Tecnicas("Amonestacion", True, 0.9, 90, 70, None)
        tecnica2 = Tecnicas("Esto esta GG", False, 0, 30, 100, "efecto de subir 1'25*DMG propio")
        tecnica3 = Tecnicas("5 min para entregar", True, 0.3, 70, 100, "efecto de subir 1'25*DMG propio")
        tecnica4 = Tecnicas("Ejercicios", True, 0.6, 40, 90, None)
        p1.setTecnicas(tecnica1, tecnica2, tecnica3, tecnica4)
        salir = True

    elif slcP == 2:
        p1 = Personaje("KHANTOSO", 700, 90, 18)
        tecnica5 = Tecnicas("Lanzadurm", True, 0.8, 90, 80, "Se cura un 5% de su vida max")
        tecnica6 = Tecnicas("No entregado el CV", True, 0.6, 40, 100, None)
        tecnica7 = Tecnicas("Movil en clase", False, 0, 70, 75, "Proximo ataque enemigo no hace efecto")
        tecnica8 = Tecnicas("Tê MàtÖ", False, 1.5, 60, 30, None)
        p1.setTecnicas(tecnica5, tecnica6, tecnica7, tecnica8)
        salir = True

    elif slcP == 3:
        p1 = Personaje("Er shico voley", 400, 250, 22)
        tecnica9 = Tecnicas("Remate en la cara", True, 0.7, 50, 90, None)
        tecnica10 = Tecnicas("Soy vegano", True, 0.4, 60, 100, "recupera 50 de mana")
        tecnica11 = Tecnicas("Ir a por el balon", False, 0, 70, 95, "efecto de bajar 0'7*DMG rival")
        tecnica12 = Tecnicas("Perraco", True, 1, 120, 85, "Le sube el ataque y el dinero")
        p1.setTecnicas(tecnica9, tecnica10, tecnica11, tecnica12)
        salir = True

    elif slcP == 4:
        p1 = Personaje("Thor-cido", 550, 111, 30)
        tecnica13 = Tecnicas("Puñetazo limpio", True, 0.8, 60, 90, None)
        tecnica14 = Tecnicas("Mirada furtiva", False, 0, 30, 100, "efecto de bajar 0'8*DMG rival")
        tecnica15 = Tecnicas("Atropoyamineto", True, 1.1, 100, 80, None)
        tecnica16 = Tecnicas("Grito de guerra", False, 0, 30, 100, "efecto de subir 1'5*DMG propio")
        p1.setTecnicas(tecnica13, tecnica14, tecnica15, tecnica16)
        salir = True

m.menuCombate()