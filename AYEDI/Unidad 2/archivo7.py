#18/08/2021
"""
El programa debe:
- pedir en orden el Nombre, apellido, edad y numero de calzado
- verificar que cada uno sea el tipo de variable correcto (IMPORTANTE)
- en caso verdadero imprimir de la siguiente manera el resultado:
"""
try:
    dato_1 = str(input("Ingrese nombre "))
    dato_2 = str(input("Ingrese apellido "))
    dato_3 = int(input("Ingrese edad "))
    dato_4 = float(input("Ingrese numero de calzado "))
    print(f"Su nombre completo es {dato_1} {dato_2}, usted tiene \n \
         {dato_3} años y calza {dato_4}")
except: 
    print("Error")