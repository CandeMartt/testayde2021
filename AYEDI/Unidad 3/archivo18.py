#25/08/2021
"""
El programa debe:
*  pedir al usuario 5 datos numericos
*  verificar que sean enteros y sino pedir nuevamente los 5
*  cuando se tenga los 5 datos el programa debe devolver el promedio
*  no deben aparecer errores.
"""
try:
    flag = True
    while flag:
        nota_1 = int(input("Ingrese 1º nota "))
        nota_2 = int(input("Ingrese 2º nota "))
        nota_3 = int(input("Ingrese 3º nota "))
        nota_4 = int(input("Ingrese 4º nota "))
        nota_5 = int(input("Ingrese 5º nota "))

        promedio = ((nota_1 + nota_2 + nota_3 + nota_4 + nota_5)/5)
        print(f"El promedio es {promedio}")   
    flag= False
except:
    print("ERROR. Datos incorrectos")

#GONZA
    print("Este programa calculará el promedio de 5 números")
i = 1
acum = 0
while i<=5:
    try:
        numero=float(input("ingrese un número"))
        i+=1
        acum+=numero
    except:
        print("no es un número válido")
        i=i
promedio = acum/5
print(f"El promedio de los cinco números ingresados es {promedio}")

