#26/08/2021
"""
El programa debe:
*     Preguntar al usuario una cantidad a invertir
*     Preguntar al usuario el interés anual y el número de años
*     Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión
"""

try:
    inversion = float(input("Ingrese la cantidad que desee invertir: "))
    interes = float(input("Ingrese es el interes anual: "))
    numero_años= int(input("Ingrese el numero de años: "))

    resultado_anual = (inversion + (inversion * interes/100))
    resultado_años = (resultado_anual * numero_años)
    print(f"El resultado en {numero_años} es {resultado_años}")
except:
    print("ERROR.")
