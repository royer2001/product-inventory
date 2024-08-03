# product-inventory

# Gestión de Productos

Este programa permite gestionar una lista de productos, incluyendo operaciones para agregar, eliminar y actualizar productos. 

## Descripción

El programa presenta un menú interactivo donde puedes:
- **Agregar** nuevos productos.
- **Eliminar** productos existentes.
- **Actualizar** detalles de productos (pendiente de implementación).
- **Salir** del programa.

## Estructura del Código

- **Productos**: Un diccionario que almacena el nombre de los productos con un identificador único.
- **Precios**: Un diccionario que almacena el precio de cada producto con su identificador único.
- **Stock**: Un diccionario que almacena la cantidad disponible de cada producto con su identificador único.

### Funciones Principales

1. **mostrar_menu()**
   - Muestra el menú con la lista de productos, precios y stock.
   - Ofrece opciones para agregar, eliminar, actualizar productos o salir del programa.

2. **generar_clave(diccionario)**
   - Genera una nueva clave para un producto, basada en el tamaño actual del diccionario.

3. **agregar_producto()**
   - Permite al usuario agregar un nuevo producto especificando el nombre, precio y cantidad.

4. **eliminar_producto()**
   - Placeholder para la funcionalidad de actualización de productos (a implementar).

5. **actualizar_producto()**
   - Placeholder para la funcionalidad de actualización de productos (a implementar).

## Uso

1. Ejecuta el programa.
2. Elige una opción del menú:
   - **1**: Agregar un nuevo producto.
   - **2**: Eliminar el primer producto en la lista.
   - **3**: Actualizar los detalles de un producto (no implementado).
   - **4**: Salir del programa.
3. Sigue las instrucciones proporcionadas en la consola para cada opción.

## Requisitos

(pendiente de agregar requisitos).

## Ejecución

Para ejecutar el programa, guarda el código en un archivo llamado `main.py` y corre el siguiente comando en la terminal:

```bash
python main.py
```

## Nota

- La función `actualizar_producto` está pendiente de implementación. Actualmente solo imprime un mensaje de lugar.
- La función `eliminar_producto` esta pendiente de implementación. Actualmente solo de manera de ejemplo elimina el primer elemento de los diccionarios.
