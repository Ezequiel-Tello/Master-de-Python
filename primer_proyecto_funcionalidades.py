"""
This module provides functions for [describe purpose of the script].
"""
# 1: Mostramos mensaje de bienvenida
print("¡Bienvenido a tu software administrativo personal!")
# 2 y 3: Pedimos al usuario que ingrese los datos requeridos y almacenamos los valores en variables
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad en stock: "))
precio = float(input("Ingrese el precio por unidad: $"))
valor_total = (cantidad * precio)
# 4 vamos a mostrar todo el inventario con la informacion de este
print("---Inventario inicial---")
print("Nombre del producto: ", (producto))
print("Cantidad en stock: ", (cantidad))
print("Precio unitario: $", (precio))
print("valor de inventario inicial: $", (valor_total))
