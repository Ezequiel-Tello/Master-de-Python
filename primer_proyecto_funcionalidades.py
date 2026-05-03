"""
This module provides functions for [describe purpose of the script].
"""
# 1: Mostramos mensaje de bienvenida
print("¡Bienvenido a tu software administrativo personal!")
# 2 y 3: Pedimos al usuario que ingrese los datos requeridos y almacenamos los valores en variables
producto = input("Ingrese el nombre del producto: ").title().strip()
cantidad = int(input("Ingrese la cantidad en stock: "))
precio = float(input("Ingrese el precio por unidad: $"))
valor_total = cantidad * precio
# 4 Vamos a mostrar todo el inventario con la informacion de este
# 5 Use f-string para formateare el valor de las variables
print("---Inventario inicial---")
print("-" * 30)
print(f"Nombre del producto               : {producto}")
print(f"Cantidad en stock                 : {cantidad}")
print(f"Precio unitario                   : ${precio:.2f}")
print(f"valor de inventario inicial       : ${valor_total:.2f}")
print("-" * 30)
# 6 Terminamos el proyecto numero 2 usando "print" con guiones como separación para una mejora visual
