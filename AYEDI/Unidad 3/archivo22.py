#26/08/2021
"""
El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca
 hasta que el usuario escriba “salir” que terminará.
 *  si el usuario escribe "hola" o "chau" que no se haga el eco
"""

while True:
    try:
        dato_1 = str(input("Introduzca una palabra. Para terminar escriba salir. ")) 
        if dato_1.lower() == "salir":
            print("Buenas noches!")
            break
        elif dato_1.lower() == "hola" or dato_1.lower() =="chau":
            continue
        else:
            print(f"Usted ingreso {dato_1}")  #ESTE SE PONE EN UN ELSE PARA QUE QUEDE MEJOR Y PARA QUE NO LO LEA EN EL HOLA NI EL CHAU
    except:
        print("ERROR.")