#26/08/2021
"""
El programa debe:
*    Pedir al usuario un número entero positivo y mostrar por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

Ej: num = 8.

8,7,6,5,4,3,2,1
"""

try:
   
    while True:
        numero = int(input("Ingrese un numero entero positivo: "))
        if numero >0:
            break
    for i in range(numero,0,-1):
        print(i)
except:
    print("ERROR.")