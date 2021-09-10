#02/09/2021
"""
###**Ejercicio 4.2 (Mediciones)**
El programa debe:
*   Contar con 4 funciones (calcular Area (cuadrado), calcular Perimetro(cuadrado),
    calcular Area (circulo), calcular Perimetro(circulo))
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
import math as mt #Para importar la libreria

def perimetro_circulo():
    while True:
        try:
            radio_circulo= float(input("Ingrese el radio del circulo: "))
            if (radio_circulo <= 0):
                print("Ingrese un radio mayor o distinto de cero")
            else:
                 break #se puede poner el return aca y salir del bucle
        except:
            print("ERROR. Datos erroneos")

    return round(2*mt.pi*radio_circulo,0),radio_circulo #se puede salir de un bucle con el return

def area_circulo():
    while True:
        try:
            radio_circulo= float(input("Ingrese el radio del circulo: "))
            if (radio_circulo<= 0):
                print("Ingrese un radio mayor o distinto de cero")
            else:
                 break 
        except:
            print("ERROR. Datos erroneos")

    return round(mt.pi*radio_circulo**2,0),radio_circulo #se puede salir de un bucle con el return

def perimetro_cuadrado():
    while True:
        try:
            lado_cuadrado= float(input("Ingrese cuanto mide un lado del cuadrado: "))
            if (lado_cuadrado <= 0):
                print("Ingrese un numero mayor o distinto de cero")
            else:
                 break 
        except:
            print("ERROR. Datos erroneos")
    print(f"El perimetro del cuadrado es {lado_cuadrado*4} cm")

   

def area_cuadrado():
    while True:
        try:
            lado_cuadrado= float(input("Ingrese cuanto mide un lado del cuadrado: "))
            if (lado_cuadrado <= 0):
                print("Ingrese un numero mayor o distinto de cero")
            else:
                 break 
        except:
            print("ERROR. Datos erroneos")
    print(f"El area del cuadrado es {lado_cuadrado*lado_cuadrado} cm")



while True:
        condicion=input(
        """Por favor ingrese la opcion que desee utilizar
            1. Perimetro de un circulo
            2. Area de un circulo
            3. Perimetro de un cuadrado
            4. Area de un cuadrado
            5. Salir
        Numero: """)
    
        if condicion =="1":   
            perimetro,radio_circulo = perimetro_circulo()
            print(f"El radio del circulo es {radio_circulo} cm y el perimetro del circulo es {perimetro} cm")  
        elif condicion =="2":   
            area,radio_circulo = area_circulo()
            print(f"El radio del circulo es {radio_circulo} cm y el area del circulo es {area} cm")
        elif condicion =="3":   
            perimetro_cuadrado()
        elif condicion =="4":   
            area_cuadrado()
        elif condicion =="5":   
            print("Gracias por utilizar esta calculadora! Hasta luego!")
            break
        else:
            print("No ingreso una opcion correcta")
        



