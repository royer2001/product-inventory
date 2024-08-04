from utils import generar_clave, mostrar_mensaje, limpiar_pantalla, alerta

Productos = {1: "Pantalones", 2: "Camisas", 3: "Corbatas", 4: "Casacas"}
Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
Stock = {1: 50, 2: 45, 3: 30, 4: 15}

opcion = None


def mostrar_menu():
    print("==============================================")
    print("Lista de Productos:")
    print("==============================================")
    print(f"{'ID'.ljust(5)} {'PRODUCTO'.ljust(15)} {'PRECIO'.ljust(15)} {'STOCK'.ljust(5)}")
    print("==============================================")

    for key in Productos:
        print(f"{str(key).ljust(5)} {Productos[key].ljust(15)} {str(Precios[key]).ljust(15)} {str(Stock[key]).ljust(5)}")

    print("==============================================")

    print("Acciones: [1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")


def agregar_producto():
    print("Agregar")

    nueva_clave = generar_clave(Productos)

    while True:
        nombre = input('Ingrese nombre: ').strip()
        if nombre:
            break
        alerta("El nombre no puede estar vacío. Intente nuevamente.")

    while True:
        precio_entrada = input('Ingrese precio: ').strip()
        if precio_entrada:
            try:
                precio = float(precio_entrada)
                break
            except ValueError:
                alerta("El precio debe ser un número válido. Intente nuevamente.")
        else:
            alerta("El precio no puede estar vacío. Intente nuevamente.")

    while True:
        cantidad_entrada = input('Ingrese cantidad: ').strip()
        if cantidad_entrada:
            try:
                cantidad = int(cantidad_entrada)
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
                break
            except ValueError as e:
                alerta(f"Entrada inválida. {e} Intente nuevamente ingresando la cantidad.")
        else:
            alerta("La cantidad no puede estar vacía. Intente nuevamente.")

    Productos[nueva_clave] = nombre
    Precios[nueva_clave] = precio
    Stock[nueva_clave] = cantidad

    limpiar_pantalla()
    mostrar_mensaje(opcion)


def eliminar_producto():
    print("Eliminar")

    id_producto = int(input("Ingrese ID del producto: "))

    if id_producto in Productos:
        Productos.pop(id_producto)
        Precios.pop(id_producto)
        Stock.pop(id_producto)
        limpiar_pantalla()
        mostrar_mensaje(opcion)
    else:
        limpiar_pantalla()
        alerta(f"Producto con ID {id_producto} no encontrado.")


def actualizar_producto():
    # TODO update products
    id_producto = int(input("Ingrese ID del producto: "))
    if id_producto in Productos:

        print(f"Editando producto con ID {id_producto}")

        while True:
            nombre = input('Ingrese Nombre: ').strip()
            if nombre:
                break
            alerta("El nombre no puede estar vacío. Intente nuevamente.")

        while True:
            precio_entrada = input('Ingrese precio: ').strip()
            if precio_entrada:
                try:
                    precio = float(precio_entrada)
                    break
                except ValueError:
                    alerta("El precio debe ser un número válido. Intente nuevamente.")
            else:
                alerta("El precio no puede estar vacío. Intente nuevamente.")

        while True:
            cantidad_entrada = input('Ingrese cantidad: ').strip()
            if cantidad_entrada:
                try:
                    cantidad = int(cantidad_entrada)
                    if cantidad < 0:
                        raise ValueError("La cantidad no puede ser negativa.")
                    break
                except ValueError as e:
                    alerta(f"Entrada inválida. {e} Intente nuevamente ingresando la cantidad.")
            else:
                alerta("La cantidad no puede estar vacía. Intente nuevamente.")

        Productos[id_producto] = nombre
        Precios[id_producto] = precio
        Stock[id_producto] = cantidad

        limpiar_pantalla()
        mostrar_mensaje(opcion)
    else:
        limpiar_pantalla()
        alerta(f"Producto con ID {id_producto} no encontrado.")


while opcion != 4:
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
            limpiar_pantalla
            mostrar_mensaje(opcion)
        else:
            limpiar_pantalla()
            alerta("Opción inválida, ingrese una de las opciones")
            raise ValueError(
                "Vuelva a intentarlo ingresando un número válido de las opciones.")
    except ValueError as e:
        limpiar_pantalla()
        alerta(f"Entrada inválida. {e}")
