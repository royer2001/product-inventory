Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

print('========================================')
print('Lista de Productos:')
print('========================================')

for key in Productos:
    print(f"{key} \t {Productos[key]} \t {Precios[key]} \t {Stock[key]}")

print('========================================')

print(f"[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir,")

try:
    option = int(input('Elija opción:'))

    if option == 1:
        print('Agregar')
    elif option == 2:
        print('Eliminar')
    elif option == 3:
        print('Actualizar')
    elif option == 4:
        print('Salir')
    else:
        print('Opción invalida, ingrese una de las opciones')
except:
    print('Entrada invalida, ingrese una de las opciones')