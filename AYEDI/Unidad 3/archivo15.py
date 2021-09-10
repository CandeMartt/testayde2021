#TAREA
"""
El programa siguiente muestra el color obtenido al mezclar dos colores en la pantalla, siendo los 3 posibles:
Azul
Rojo
Verde
Y los posibles resultados son:
"""

try:
    dato_1 = str(input("Por favor elija entre el color rojo o azul "))
    dato_2 = str(input("""Si usted eligio el rojo ahora debe elegir entre:
    -Azul
    -Verde
    Si usted eligio el azul ahora deberá elegir entre:
    -Verde
    -Rojo
    Ingreso: """))

    if dato_1.lower()== "rojo": #Para saber que color eligió en la primera opcion
        if dato_1.lower()== "rojo" and dato_2.lower() == "azul" : #Para saber que combinación de colores eligio
            print(f"La combinacion de {dato_1} y {dato_2} es morado ")
        elif dato_1.lower() == "rojo" and dato_2.lower() == "verde": #Para saber que combinación de colores eligio
            print(f"La combiancion {dato_1} y {dato_2} es amarilla")
        else:
            print("Usted no escribio ninguna de las dos opciones")
    elif dato_1.lower()== "azul": #Para saber que color eligió en la primera opcion
        if dato_1.lower() == "azul" and dato_2.lower() == "verde": #Para saber que combinación de colores eligio
            print(f"La combinacion de {dato_1} y {dato_2} es Cyan")
        elif dato_1.lower() == "azul" and dato_2.lower()== "rojo": #Para saber que combinación de colores eligio
            print(f"La combiancion de {dato_1} y {dato_2} es morada.")  
        else:
            print("No ingreso bien el color")
    else:
        print("Usted no ingresó ninguna de las opciones. Vuelva a intentarlo.") #Saldrá si el usuario no eligió ni el color rojo ni el azul
except:
    print("ERROR.")
