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
