from os import system

Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

option = None

def mostrar_menu():
    print('========================================')
    print('Lista de Productos:')
    print('========================================')

    for key in Productos:
        print(f"{key} \t {Productos[key]} \t {Precios[key]} \t {Stock[key]}")

    print('========================================')

    print(f"[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir,")

def generar_clave(diccionario):
    return len(diccionario) + 1

def agregar_producto():
    print('Agregar')
    nombre = input('Ingrese Nombre: ')
    precio = input('Ingrese Precio: ')
    cantidad = int(input('Ingrese Cantidad: '))

    Productos[generar_clave(Productos)] = nombre
    Precios[generar_clave(Precios)] = precio
    Stock[generar_clave(Stock)] = cantidad
    system("cls")
    print("*** Agregado Exitosamente ***")

def eliminar_producto():
    print('Eliminar')

    print(Productos.pop(1, 'No encontrado'))
    Precios.pop(1, 'No encontrado')
    Stock.pop(1, 'No encontrado')

    print('Eliminado exitosamente')

def actualizar_producto():
    # TODO update products
    print('actualizar')

while option != 4:
    mostrar_menu()

    try:
        option = int(input('Elija opción:'))

        if option == 1:

            agregar_producto()

        elif option == 2:
            
            eliminar_producto()

        elif option == 3:
            actualizar_producto()
        elif option == 4:
            print('Saliendo del programa...')
        else:
            print('Opción invalida, ingrese una de las opciones')
    except:
        print('Entrada invalida, ingrese un número de las opciones')
