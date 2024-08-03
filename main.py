from utils import generar_clave, mostrar_mensaje, limpiar_pantalla

Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

opcion = None

def mostrar_menu():
    print('==================================================')
    print('Lista de Productos:')
    print('==================================================')

    print(f"ID \t PRODUCTO \t PRECIO \t STOCK")
    print('==================================================')

    for key in Productos:
        print(f"{key} \t {Productos[key]} \t {Precios[key]} \t\t {Stock[key]}")

    print('==================================================')

    print(f"[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir,")


def agregar_producto():
    print('Agregar')
    nombre = input('Ingrese Nombre: ')
    precio = float(input('Ingrese Precio: '))
    cantidad = int(input('Ingrese Cantidad: '))
    nueva_clave = generar_clave(Productos)

    Productos[nueva_clave] = nombre
    Precios[nueva_clave] = precio
    Stock[nueva_clave] = cantidad
    
    limpiar_pantalla()
    mostrar_mensaje(opcion)

def eliminar_producto():
    print('Eliminar')

    id_producto = int(input('Ingrese ID del producto: '))

    if id_producto in Productos:
        Productos.pop(id_producto)
        Precios.pop(id_producto)
        Stock.pop(id_producto)
        limpiar_pantalla()
        mostrar_mensaje(opcion)
    else:
        limpiar_pantalla()
        print(f'Producto con ID {id_producto} no encontrado.')

def actualizar_producto():
    # TODO update products
    id_producto = int(input('Ingrese ID del producto: '))
    if id_producto in Productos:

        print(f'Editando producto con ID {id_producto}')

        nombre = input('Ingrese Nombre: ')
        precio = float(input('Ingrese Precio: '))
        cantidad = int(input('Ingrese Cantidad: '))

        Productos[id_producto] = nombre
        Precios[id_producto] = precio
        Stock[id_producto] = cantidad

        limpiar_pantalla()
        mostrar_mensaje(opcion)
    else:
        limpiar_pantalla()
        print(f'Producto con ID {id_producto} no encontrado.')

while opcion != 4:
    mostrar_menu()

    try:
        opcion = int(input('Elija opción:'))

        if opcion == 1:
            agregar_producto()

        elif opcion == 2:
            eliminar_producto()

        elif opcion == 3:
            actualizar_producto()

        elif opcion == 4:
            mostrar_mensaje(opcion)
        else:
            print('Opción invalida, ingrese una de las opciones')
    except:
        print('Entrada invalida, ingrese un número de las opciones')
