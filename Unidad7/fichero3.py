"""
#### **Ejercicio 7.3**
Crear una funcion para leer el un archivo.txt.

Crear funciones para:
*   Contar la cantidad de letrar que tiene el archivo (letras no espacios ni puntos)
*   Contar la cantidad de palabras que tiene el archivo
"""
"""try:
    fichero = open ("archivo3.txt",'r')
    letra = fichero.readline(1)
    acum = 0
    while (letra !=""):
        letra = fichero.readline(1)
        
        if((letra >= "a" and letra <= "z") or (letra >= "A" and letra <= "Z")):
            acum += 1

    fichero.close()
    print(acum)

except:
        print("no existe el archivo")"""

try:
    fichero = open ("archivo3.txt",'r')
    acum = 0
    while True: 
        letra = fichero.readline(1)   
        if letra == "":
            break
        elif(letra != "." and letra != " "):
            acum += 1
    fichero.close()
    print(acum)

except:
        print("no existe el archivo")