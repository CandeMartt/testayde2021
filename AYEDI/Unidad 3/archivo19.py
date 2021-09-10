#25/08/2021
"""
El programa debe:

pedir al usuario una palabra
pedir un numero al usuario
mostrar la palabra por pantalla la cantidad de veces que diga el numero
no debe generar errores
"""

try:
    dato_1 = str(input("Ingrese una palabra"))
    dato_2 = int(input("Ingrese un numero"))
    if dato_1.isalpha():
        i=1
        while i <= dato_2:
            print(f"{dato_1} {i}")
            i+=1
except:
    print("Error. Dato incorrecto")