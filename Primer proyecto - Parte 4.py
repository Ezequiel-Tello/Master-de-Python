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
            print(" ")
            for i, prod in enumerate(inventario):
                if prod['nombre'] == nombre:
                    inventario.pop(i)
                    print(" ")
                    print(
                        "********************** PRODUCTO ELIMINADO **********************")
                    print(" ")
                    break
            else:
                print(" ")
                print("******************** PRODUCTO NO ENCONTRADO ********************")
                print(" ")
        elif opcion == 3:
            if not inventario:
                print(" ")
                print("*********************** INVENTARIO VACIO ***********************")
                print(" ")
            else:
                for prod in inventario:
                    print("*" * 30)
                    print(
                        f"Nombre del producto               : {prod['nombre']}")
                    print(
                        f"Cantidad en stock                 : {prod['cantidad']}")
                    print(
                        f"Precio unitario                   : ${prod['precio']:.2f}")
                    print(
                        f"valor de inventario inicial       : ${prod['valor_total']:.2f}")
                    print("*" * 30)
        elif opcion == 4:
            print(" ")
            print("********************** PROGRAMA FINALIZADO **********************")
            print(" ")
            break
        else:
            print("Opción inválida")
