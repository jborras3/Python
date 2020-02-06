import Personaje
import Tecnicas
from Batalla import Batalla
import time


print("   ___             _       _        _                    __  __  ")
print("  | _ )   __ _    | |_    | |_     | |     ___     ___  |  \/  |   ___    _ __     ___ ")
print("  | _ \  / _` |   |  _|   |  _|    | |    / -_)   |___| | |\/| |  / -_)  | '  \   / -_) ")
print("  |___/  \__,_|   _\__|   _\__|   _|_|_   \___|   _____ |_|__|_|  \___|  |_|_|_|  \___|  ")
print("_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|     |_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"| ")
print("\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'")
print("                                         Welcome")

time.sleep(3.5)

Batalla.menuEligePersonaje()

while False:
    slcP = input()
    #Crear las clases a partir de variables
    #Crear metodo para introducir los valores en variables
    #con el mismo nombre de entrada del constructor
    if slcP == 1:
        p1 = Personaje()
        break

    elif slcP == 2:
        break

    elif slcP == 3:
        break

    elif slcP == 4:
        break