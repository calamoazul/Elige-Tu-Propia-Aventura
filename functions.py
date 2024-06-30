
import os
# Función para marcar el fin del juego
def game_over():
    print("/***GAME OVER***/\n")
    input("Pulsa cualquier tecla para salir del programa")

# Función para indicar el paso de nivel

def next_level():
    print("/*** Has superado el nivel ***/\n")
    input("Pulsa cualquier tecla para continuar")

# Función para escoger opciones

def choose_option():
    option = input("¿Qué opción escoges? ")
    if(option.upper() == "A"):
        return "A"
    elif(option.upper() == "B"):
        return "B"
    else:
        print("No has escogido una opción correcta")
        choose_option()


def clear_console():
    if(os.name == "posix"):
        return os.system("clear")
    elif(os.name == ("ce", "nt", "dos")):
        return os.system("cls")