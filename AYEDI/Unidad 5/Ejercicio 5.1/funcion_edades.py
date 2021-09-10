"""Crear una funcion que debe: (usar listas)

*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

def funcion_edades():
    try:
        dato_1 = int(input("Ingrese la cantidad de personas "))   
        i = 1
        acum = 0
        while i<= dato_1:
            dato_2 = int(input(f"Ingrese la edad de {i}.  "))
            i += 1
            acum += dato_2
        for i in acum+1:
            if i > acum:
                print(f"La edad {i} es mayor")  
    except:
        print("ERROR.")    