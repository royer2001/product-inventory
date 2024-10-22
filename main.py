from Product import ProductException
from utils import mostrar_mensaje, limpiar_pantalla, alerta

from Inventory import Inventory

o_inventory = Inventory()

#Datos iniciales
Productos = {1: "Pantalones", 2: "Camisas", 3: "Corbatas", 4: "Casacas"}
Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
Stock = {1: 50, 2: 45, 3: 30, 4: 15}

#Conviertiendo datos en un listado de objetos
for key in Productos:
    o_inventory.create_product(Productos[key], Precios[key], Stock[key])

def mostrar_menu():
    print("==============================================")
    print("Lista de Productos:")
    print("==============================================")
    print(f"{'ID'.ljust(5)} {'PRODUCTO'.ljust(15)} {'PRECIO'.ljust(15)} {'STOCK'.ljust(5)}")
    print("==============================================")
    o_inventory.show_list()
    print("==============================================")
    print("Acciones: [1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")

def agregar_producto():
    o_inventory.add_product()
    limpiar_pantalla()
    mostrar_mensaje(opcion)

def eliminar_producto():
    o_inventory.delete_product()
    limpiar_pantalla()
    mostrar_mensaje(opcion)

def actualizar_producto():
    o_inventory.edit_product()
    limpiar_pantalla()
    mostrar_mensaje(opcion)

# manejo de opciones del menu
opcion = None

#interfaz del programa
while True:
    mostrar_menu()

    try:
        opcion = int(input("Elija opción:"))

        if opcion == 1:
            agregar_producto()

        elif opcion == 2:
            eliminar_producto()

        elif opcion == 3:
            actualizar_producto()

        elif opcion == 4:
            limpiar_pantalla()
            mostrar_mensaje(opcion)
            break
        else:
            limpiar_pantalla()
            alerta("Opción inválida, ingrese una de las opciones")
            raise ValueError("Vuelva a intentarlo ingresando un número válido de las opciones.")
    except ProductException as e:
        limpiar_pantalla()
        alerta(f"Error: {e}")
