# Creamos una lista donde se va a guardar las variables con sus respectivos datos
Inventario = []
# Mostramos mensaje de bienvenida
print("------------------------------------------------------------")
print("-----¡Bienvenido a tu software administrativo personal!-----")
print("------------------------------------------------------------")

# Pedimos al usuario que ingrese el primer producto y almacenamos los valores en variables
producto1 = input("Ingrese el nombre del primer producto: ").title().strip()
cantidad1 = int(input("Ingrese la cantidad en stock: "))
precio1 = float(input("Ingrese el precio por unidad: $"))
valor_total1 = cantidad1 * precio1
# Creamos el diccionario 1 para el primer producto
producto_dict1 = {
    "nombre": producto1,
    "cantidad": cantidad1,
    "precio": precio1,
    "valor_total": valor_total1
}
# Usamos .append() para introducir "producto_dict1" al "inventario"
Inventario.append(producto_dict1)

# Pedimos al usuario que ingrese los datos del 2do producto y volvemos a almacenar los valores en variables
producto2 = input("Ingrese el nombre del segundo producto: ").title().strip()
cantidad2 = int(input("Ingrese la cantidad en stock: "))
precio2 = float(input("Ingrese el precio por unidad: $"))
valor_total2 = cantidad2 * precio2
# Creamos el diccionario 2 para el segundo producto
producto_dict2 = {
    "nombre": producto2,
    "cantidad": cantidad2,
    "precio": precio2,
    "valor_total": valor_total2
}
# Usamos .append() para introducir "produco_dict2" al "inventario"
Inventario.append(producto_dict2)

# Solicitamos un tercer producto al usuario
producto3 = input("Ingrese el nombre del tercer producto: ").title().strip()
cantidad3 = int(input("Ingrese la cantidad en stock: "))
precio3 = float(input("Ingrese el precio por unidad: $"))
valor_total3 = cantidad3 * precio3
# Creamos el diccionario 3 para el tercer producto
producto_dict3 = {
    "nombre": producto3,
    "cantidad": cantidad3,
    "precio": precio3,
    "valor_total": valor_total3
}
# Usamos .append() para introducir "produco_dict3" al "inventario"
Inventario.append(producto_dict3)

#  Vamos a mostrar todo el inventario con la informacion de este
#  Usanmos f-string para formateare el valor de las variables
print("-" * 30)
print("------Inventario inicial------")
print("-" * 30)
print("")
print(f"Nombre del producto               : {Inventario[0]['nombre']}")
print(f"Cantidad en stock                 : {Inventario[0]['cantidad']}")
print(f"Precio unitario                   : ${Inventario[0]['precio']:.2f}")
print(
    f"valor de inventario inicial       : ${Inventario[0]['valor_total']:.2f}")
print(" ")
print("-" * 30)
print("-" * 30)
print(" ")
print(f"Nombre del producto               : {Inventario[1]['nombre']}")
print(f"Cantidad en stock                 : {Inventario[1]['cantidad']}")
print(f"Precio unitario                   : ${Inventario[1]['precio']:.2f}")
print(
    f"valor de inventario inicial       : ${Inventario[1]['valor_total']:.2f}")
print("-" * 30)
print("-" * 30)
print("")
print("")
print(f"Nombre del producto               : {Inventario[2]['nombre']}")
print(f"Cantidad en stock                 : {Inventario[2]['cantidad']}")
print(f"Precio unitario                   : ${Inventario[2]['precio']:.2f}")
print(
    f"valor de inventario inicial       : ${Inventario[2]['valor_total']:.2f}")
print("-" * 30)
print("-" * 30)
