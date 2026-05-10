"""Software administrativo personal para gestión de inventario."""

LOGIN = "Estudiante"
PASSWORD = "AcademiaDaxusLatam"
bandera = False
inventario = []
print("************************************************************")
print("**** ¡BIENVENIDO A TU SOFTWARE ADMINISTRATIVO PERSONAL! ****")
print("************************************************************")

for i in range(3):
    Usuario = input("Ingrese su usuario: ")
    Pass = input("Ingrese la contraseña: ")

    if Usuario == LOGIN and Pass == PASSWORD:
        bandera = True
        print("Usuario valido")
        break
    else:
        print("Usuario o contraseña invalida, intente nuevamente")
print(" ")
if bandera:
    print("********************** MENÚ PRINCIPAL **********************")
    print(" ")
    opcion = 0
    while opcion != 4:
        print("1. Agregar producto al inventario")
        print("2. Eliminar producto del inventario")
        print("3. Mostrar inventario")
        print("4. Salir")
        print(" ")
        opcion = int(input("elija una opción: "))
        print(" ")
        if opcion == 1:
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
                    print(" ")
                elif opcion_add == "2":
                    break
                else:
                    print("Opción inválida, ingrese 1 o 2")
        elif opcion == 2:
            nombre = input(
                "Ingrese el nombre del producto a eliminar: ").title().strip()
            for i, prod in enumerate(inventario):
                if prod['nombre'] == nombre:
                    inventario.pop(i)
                    print("Producto eliminado")
                    break
            else:
                print(" ")
                print("*****Producto no encontrado*****")
                print(" ")
        elif opcion == 3:
            if not inventario:
                print(" ")
                print("*****Inventario vacío*****")
                print(" ")
            else:
                for prod in inventario:
                    print(" ")
                    print(
                        f"Nombre: {prod['nombre']}, Cantidad: {prod['cantidad']}, Precio: ${prod['precio']:.2f}, Valor total: ${prod['valor_total']:.2f}")
                    print(" ")
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")
