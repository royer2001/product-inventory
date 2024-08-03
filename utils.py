import os


def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def generar_clave(diccionario):
    if diccionario:
        return max(diccionario.keys()) +1
    else:
        return 1
    
def mostrar_mensaje(opcion):
    mensajes = {
        1:'*** Agregado exitosamente ***', 
        2:'*** Eliminado correctamente ***', 
        3:'*** Actualizado correctamente ***', 
        4:'*** Saliendo del programa ***'
    }
    mensaje = mensajes.get(opcion, 'Opcion no encontrada')
    print(mensaje)
