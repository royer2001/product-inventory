# Repositorio -> product-inventory

# Gestión de Productos

Este programa permite gestionar una lista de productos en una tienda, proporcionando funcionalidades para agregar, eliminar y actualizar productos. Utiliza un menú interactivo para la gestión de productos.

## Descripción

El programa proporciona las siguientes opciones:
- **Agregar**: Añadir un nuevo producto especificando nombre, precio y cantidad.
- **Eliminar**: Eliminar un producto existente utilizando su ID.
- **Actualizar**: Modificar los detalles de un producto existente.
- **Salir**: Finalizar la ejecución del programa.

## Estructura del Código

- **Productos**: Diccionario que almacena los nombres de los productos con un identificador único.
- **Precios**: Diccionario que almacena los precios de los productos con su identificador único.
- **Stock**: Diccionario que almacena la cantidad disponible de cada producto con su identificador único.

### Funciones Principales

1. **mostrar_menu()**
   - Muestra el menú con la lista de productos, precios y stock.
   - Ofrece opciones para agregar, eliminar, actualizar productos o salir del programa.

2. **agregar_producto()**
   - Permite al usuario agregar un nuevo producto solicitando nombre, precio y cantidad.
   - Valida las entradas para asegurar que no estén vacías y que el precio y la cantidad sean valores válidos.

3. **eliminar_producto()**
   - Elimina un producto existente dado su ID.
   - Notifica si el producto no se encuentra.

4. **actualizar_producto()**
   - Permite al usuario actualizar los detalles de un producto existente.
   - Solicita ID del producto y luego actualiza nombre, precio y cantidad después de validaciones.

### Funciones del Archivo `utils.py`
  
1. **limpiar_pantalla()**
   - Limpia la pantalla de la consola.
   - Usa `cls` en sistemas Windows y `clear` en sistemas Unix.

2. **generar_clave(diccionario)**
   - Genera una nueva clave para un producto, basada en la clave máxima existente en el diccionario más uno. Si el diccionario está vacío, retorna 1.

3. **mostrar_mensaje(opcion)**
   - Muestra un mensaje de confirmación basado en la opción proporcionada:
     - **1**: Agregado exitosamente (verde).
     - **2**: Eliminado exitosamente (rojo).
     - **3**: Actualizado exitosamente (verde).
     - **4**: Saliendo del programa (magenta).
   - Si la opción no es válida, muestra "Opción no encontrada".

4. **alerta(mensaje)**
   - Muestra un mensaje de alerta en color amarillo.

## Uso

1. Ejecuta el programa.
2. Selecciona una opción del menú:
   - **1**: Agregar un nuevo producto.
   - **2**: Eliminar un producto existente.
   - **3**: Actualizar los detalles de un producto.
   - **4**: Salir del programa.
3. Sigue las instrucciones proporcionadas en la consola para cada opción.

## Requisitos

- Python 3.x.
- El script `utils.py` debe estar en el mismo directorio que el archivo principal.

## Ejecución

Guarda el código en un archivo llamado `main.py` y el archivo `utils.py` en el mismo directorio. Luego, ejecuta el programa con:

```bash
python main.py
```

## Nota

- La función `actualizar_producto` permite editar productos existentes. Asegúrate de ingresar un ID válido.