# Configuración inicial
LOGIN = "Estudiante"
PASSWORD = "AcademiaDaxusLatam"
bandera = False
inventario = []

print("************************************************************")
print("**** ¡BIENVENIDO A TU SOFTWARE ADMINISTRATIVO PERSONAL! ****")
print("************************************************************")

# Autenticación
for i in range(3):
    Usuario = input("Ingrese su usuario: ")
    Pass = input("Ingrese la contraseña: ")
    if Usuario == LOGIN and Pass == PASSWORD:
        bandera = True
        print("Usuario válido\n")
        break
    else:
        print(f"Usuario o contraseña inválida. Intentos restantes: {2-i}\n")

# Menú Principal
if bandera:
    opcion = 0
    while opcion != 4:
        print("********************** MENÚ PRINCIPAL **********************")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")

        try:
            opcion = int(input("Elija una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            while True:
                opcion_add = input(
                    "\n¿Desea agregar un producto? (1: Sí, 2: No): ").strip()
                if opcion_add == "1":  # Corregido: comparación como string
                    producto = input("Nombre del producto: ").title().strip()
                    cantidad = int(input("Cantidad en stock: "))
                    precio = float(input("Precio por unidad: $"))

                    producto_dict = {
                        "nombre": producto,
                        "cantidad": cantidad,
                        "precio": precio,
                        "valor_total": cantidad * precio
                    }
                    inventario.append(producto_dict)
                    print("¡Producto agregado!")
                elif opcion_add == "2":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == 2:
            nombre = input("Nombre del producto a eliminar: ").title().strip()
            encontrado = False
            for i, prod in enumerate(inventario):
                if prod["nombre"] == nombre:
                    inventario.pop(i)
                    print(f"--- {nombre} eliminado con éxito ---")
                    encontrado = True
                    break
            if not encontrado:
                print("\n***** Producto no encontrado *****\n")

        elif opcion == 3:
            if not inventario:
                print("\n***** Inventario vacío *****\n")
            else:
                print("\n--- ESTADO ACTUAL DEL INVENTARIO ---")
                for prod in inventario:
                    print(
                        f"Producto: {prod['nombre']} | Cantidad: {prod['cantidad']} | Precio: ${prod['precio']:.2f} | Total: ${prod['valor_total']:.2f}")
                print("------------------------------------\n")

        elif opcion == 4:
            print("Saliendo del programa... ¡Hasta pronto!")
