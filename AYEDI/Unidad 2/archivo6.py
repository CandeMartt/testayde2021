#18/08/2021
"""
El programa debe:
- pedir dos datos por consola
- verificar que los dos datos sean numeros enteros
- en caso verdadero imprimir la suma de ambos
- en caso contrario imprimir error
"""

try:
    dato_1 = int(input("Ingrese un número entero "))
    dato_2 = int(input("Ingrese otro número entero "))
    suma = dato_1 + dato_2
    print(f"El resultado de la suma es {suma}")
except:
     print("Error. Por favor ingrese un numero entero.")

