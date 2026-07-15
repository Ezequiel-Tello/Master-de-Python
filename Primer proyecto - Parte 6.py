"""Software administrativo personal para gestión de inventario."""

# --- VARIABLES GLOBALES ---
LOGIN = "Pipe"
PASSWORD = "TeAmoHijo"
inventario = []

# --- FUNCIONES DE AUTENTICACIÓN ---


def login_usuario():
    """Maneja el sistema de acceso con 3 intentos máximos."""
    print("************************************************************")
    print("**** ¡BIENVENIDO A TU SOFTWARE ADMINISTRATIVO PERSONAL! ****")
    print("************************************************************")

    for i in range(3):
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese la contraseña: ")

        if usuario == LOGIN and contraseña == PASSWORD:
            print("Usuario valido\n")
            break  # Rompe el ciclo e ignora el bloque 'else'
        else:
            print(
                f"Usuario o contraseña invalida. Intentos restantes: {2 - i}")
    else:
        # Se ejecuta solo si el for completa sus 3 vueltas
        print("\nHas agotado tus 3 intentos. El programa se cerrará.")
        exit()

# --- FUNCIONES DEL INVENTARIO ---


def agregar_producto():
    """Maneja el submenú para añadir nuevos productos al inventario."""
    while True:
        opcion_add = input(
            "¿Desea agregar un producto al inventario? (1: Sí, 2: No): ").strip()
        print(" ")

        if opcion_add == "1":
            producto = input(
                "Ingrese el nombre del producto: ").title().strip()
            cantidad = int(input("Ingrese la cantidad en stock: "))
            precio = float(input("Ingrese el precio por unidad: $"))
            valor_total = cantidad * precio

            producto_dict = {
                "nombre": producto,
                "cantidad": cantidad,
                "precio": precio,
                "valor_total": valor_total
            }
            inventario.append(producto_dict)
            print(f"¡{producto} agregado con éxito!\n")
        elif opcion_add == "2":
            break
        else:
            print("Opción inválida, ingrese 1 o 2\n")


def eliminar_producto():
    """Busca un producto por su nombre y lo elimina de la lista."""
    nombre = input(
        "Ingrese el nombre del producto a eliminar: ").title().strip()
    print(" ")

    for i, prod in enumerate(inventario):
        if prod['nombre'] == nombre:
            inventario.pop(i)
            print("\n********************** PRODUCTO ELIMINADO **********************\n")
            break
    else:
        print("\n******************** PRODUCTO NO ENCONTRADO ********************\n")


def mostrar_inventario():
    """Despliega de manera ordenada todos los artículos registrados."""
    if not inventario:
        print("\n*********************** INVENTARIO VACIO ***********************\n")
    else:
        for prod in inventario:
            print("*" * 45)
            print(f"Nombre del producto         : {prod['nombre']}")
            print(f"Cantidad en stock           : {prod['cantidad']}")
            print(f"Precio unitario             : ${prod['precio']:.2f}")
            print(f"Valor de inventario inicial : ${prod['valor_total']:.2f}")
            print("*" * 45)
        print(" ")

# --- CONTROLADOR DEL MENÚ PRINCIPAL ---


def menu_principal():
    """Muestra el menú interactivo y distribuye el flujo hacia las funciones."""
    print("************************************************************")
    print("********************** MENÚ PRINCIPAL **********************")
    print("************************************************************")
    print(" ")

    opcion = 0
    while opcion != 4:
        print("1. Agregar producto al inventario")
        print("2. Eliminar producto del inventario")
        print("3. Mostrar inventario")
        print("4. Salir")
        print(" ")

        opcion = int(input("Elija una opción: "))
        print(" ")

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            eliminar_producto()
        elif opcion == 3:
            mostrar_inventario()
        elif opcion == 4:
            print("\n********************** PROGRAMA FINALIZADO **********************\n")
            break
        else:
            print("Opción inválida\n")


# ============================================================
#               BLOQUE DE EJECUCIÓN PRINCIPAL
# ============================================================

# 1. Primero obligamos al usuario a loguearse
login_usuario()

# 2. Si el login no cortó el programa con exit(), entramos al menú
menu_principal()
