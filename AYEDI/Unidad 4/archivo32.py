#01/09/2021
"""
**Ejercicio 4.1 (Calculadora)**
El programa debe:
*   Contar con 4 funciones (suma, resta, división y multiplicación)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos numero para operar y devolver el resultado al usuario
*   Gestionar posibles errores
"""

def suma(a,b):
    try:
        suma = float(a) + float(b)
        print(f"La suma de {a} y {b} es {suma}")
    except:
        print("ERROR. Arguementos malos")

def resta(a,b):
    try:
        resta = float(a) - float(b)
        print(f"La resta de {a} y {b} es {resta}")
    except:
        print("ERROR. Arguementos malos")

def multiplicacion (a,b):
    try:
        multiplicacion = float(a) * float(b)
        print(f"La multiplicacion de {a} y {b} es {multiplicacion}")
    except:
        print("ERROR. Arguementos malos")
def division (a,b): 
    if b == 0:
            while True:
                b= input("Por favor ingrese un numero distinto a cero ")
                break
    try:
        division = float(a) / float(b)
        print(f"La division de {a} y {b} es {division}")
    except:
        print("ERROR. Arguementos malos")
def pedir_numeros():
    while True:
        try:
            num1= float(input("1º Número:"))
            num2= float(input("2º Número:"))
            break
        except:
            print("Numeros incorrectos")
    return num1, num2

while True:
        condicion=input(
        """Por favor ingrese la opcion que desee utilizar
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Salir
        Numero: """)
    
        if condicion =="1":   
            a,b = pedir_numeros()
            suma(a,b)
            
        elif condicion =="2":   
            a,b = pedir_numeros()
            resta(a,b)
           
        elif condicion =="3":   
            a,b = pedir_numeros()
            multiplicacion(a,b)

        elif condicion =="4":   
            a,b = pedir_numeros()
            division(a,b)
        elif condicion =="5":   
            print("Gracias por utilizar esta calculadora! Hasta luego!")
            break
        else:
            print("No ingreso una opcion correcta")
        
 