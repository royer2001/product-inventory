from Product import ProductException
from utils import mostrar_mensaje, limpiar_pantalla, alerta
from Inventory import Inventory

o_inventory = Inventory()

# initial data
Productos = {1: "Pantalones", 2: "Camisas", 3: "Corbatas", 4: "Casacas"}
Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
Stock = {1: 50, 2: 45, 3: 30, 4: 15}

# convert to objects
for key in Productos:
    o_inventory.create_product(Productos[key], Precios[key], Stock[key])


def show_menu():
    print("=" * 46)
    print("Lista de Productos:")
    print("=" * 46)
    print(f"{'ID'.ljust(5)} {'PRODUCTO'.ljust(15)} {'PRECIO'.ljust(15)} {'STOCK'.ljust(5)}")
    print("=" * 46)
    o_inventory.show_list()
    print("=" * 46)
    print("Acciones: [1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")


def agregar_producto():
    o_inventory.add_product()
    limpiar_pantalla()
    mostrar_mensaje(option)


def eliminar_producto():
    o_inventory.delete_product()
    limpiar_pantalla()
    mostrar_mensaje(option)


def actualizar_producto():
    o_inventory.edit_product()
    limpiar_pantalla()
    mostrar_mensaje(option)


# manejo de opciones del menu
option = None

# Main screen
while True:
    show_menu()

    try:
        option = int(input("Elija opción:"))

        if option == 1:
            agregar_producto()

        elif option == 2:
            eliminar_producto()

        elif option == 3:
            actualizar_producto()

        elif option == 4:
            limpiar_pantalla()
            mostrar_mensaje(option)
            break
        else:
            limpiar_pantalla()
            alerta("Opción inválida. ingrese una de las opciones")
    except ValueError:
        limpiar_pantalla()
        alerta("Vuelva a intentarlo ingresando un número válido de las opciones.")
    except ProductException as e:
        limpiar_pantalla()
        alerta(f"Error: {e}")