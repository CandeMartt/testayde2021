#30/09/2021
"""
##**Ejercicio 5.14**
Crear una funcion que debe: (usar diccionario)
*    Crear un diccionario vacío y lo vaya llenado con información sobre una persona
 (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
*    Pida al usuario el dato a agregar (key) y el valor
*    Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

personas = {}
def agregar_informacion():
    while True:
        key = input("Ingrese la informacion que registará o salir(para abandonar el programa): ").casefold().capitalize()
        if key == "salir":
            break
        if key in personas:
            print("Ya existe el valor, ingrese uno diferente.")
        else: 
            valor = input(f"Por favor ingrese el valor de {key}: ")
            personas.setdefault(key,valor) #el update agregaria valor y lo cambiaria y no nos intereza hacer eso ahora
            print(personas)


def imprimir_diccionario(nombre, personas):
    print(f"------------------{nombre}------------")
    print(f"--------Key\tValor--------")
    for i in personas:
        print(f"  {i}\t{personas.get(i)}")

def imprimir_diccionario_2(nombre, personas):
    #key, valores =personas.items()
    print(f"------------------{nombre}------------")
    print(f"--------Key\tValor--------")
    for i,j in personas.items():
        print(f"  {i}\t{j}")

    #print(key) #son tuplas porque no podemos modificarlas
    #print(valores)    

agregar_informacion()
imprimir_diccionario("Datos de la persona", personas)