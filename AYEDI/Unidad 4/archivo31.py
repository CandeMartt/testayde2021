#01/09/2021 FUNCIONES:como un subproceso en pseint.
#Es secuencial. Primero se declara la funcion antes de que se use
def hola_mundo():
    print("Hola Mundo!")

def suma(a,b):
    try:
        suma = int(a) + int(b)
        print(f"La suma de {a} y {b} es {suma}")
    except:
        print("ERROR. Arguemntos malos")

def suma(a,b):
    return a+b

hola_mundo()

suma(9,3)

print(f"La suma de {2} y {3} es: {suma(2,3)}")