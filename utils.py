import os

RED = "\033[31m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
YELLOW = "\033[33m"

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def generar_clave(diccionario):
    if diccionario:
        return max(diccionario.keys()) + 1
    else:
        return 1


def mostrar_mensaje(opcion):
    mensajes = {
        1: f"{GREEN}*** Agregado exitosamente ***",
        2: f"{RED}*** Eliminado exitosamente ***",
        3: f"{GREEN}*** Actualizado exitosamente ***",
        4: f"{MAGENTA}*** Saliendo del programa ***",
    }
    mensaje = mensajes.get(opcion, "Opción no encontrada")
    print(f'{mensaje}{RESET}')

def alerta(mensaje):
    print(f'{YELLOW}{mensaje}{RESET}')