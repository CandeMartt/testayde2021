"""
#### **Ejercicio 7.6**
Crear una funcion que lo que le pida palabras al usuario 
y que las vaya escribiendo en un archivo txt cada palabra una bajo la otra."""

import os
from posixpath import split
#path actual
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
path_archivo = path+"\\archivo.txt"
print(path+"\\archivo.txt")##\\ por caracteres especiales

def escribir_en_archivo(palabra):
    try:
        fichero = open(path_archivo, 'a')
        fichero.write(palabra+"\n")
        fichero.close()
    except:
        print("ERROR.")

def pedir_palabra():
    while True:
        palabra = input("Ingrese la palabra('exit' para salir): ")
        if palabra == "exit":
            break
        else:
            escribir_en_archivo(palabra)

pedir_palabra()