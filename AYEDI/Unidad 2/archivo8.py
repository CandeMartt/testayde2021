#18/08/2021
"""
El programa debe:

*   Pedir al usuario 3 notas de 3 parciales diferentes
*   verificar que los ingresados sean correctos
*   En caso correcto imprimir el promedio
*   En caso contrario imprimir un error
"""

try:
    dato_1 = float(input("Ingrese una nota "))
    dato_2 = float(input("Ingrese otra nota "))
    dato_3 = float(input("Ingrese otra nota "))
    promedio = round(((dato_1 + dato_2 + dato_3) / 3),2)
    print(f"El promedio de las notas es {promedio}")
except:
    print("ERROR")