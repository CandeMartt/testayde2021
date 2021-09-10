#19/08/2021
"""
El programa debe :
*    Pedir al usuario un string
*    Determinar si una cadena esta en minusculas o mayusculas
"""

try:
    dato_1 = str(input("Ingrese una palabra u oracion "))
    if dato_1.islower():
        print("Su oración o palabra esta en minuscula")
    else:
        print("Su palabra u oracion no esta todo en minusculas")
except: 
    print("ERROR.")