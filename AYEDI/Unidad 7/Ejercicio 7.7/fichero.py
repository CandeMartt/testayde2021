"""
#### **Ejercicio 7.7**
Crear una programa con cuatro opciones:
1.  Crear un archivo en blanco, con el nombre que desee el usuario
2.  Escribir datos en el archivo sin pisar los existentes
3.  borrar los datos del archivo
4.  leer linea a linea el archivo
"""
import os
from posixpath import split
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path_archivo = path+"\\archivo.txt"
#print(path+"\\archivo.txt")

def crear_archivo():
    nombre = input("Ingrese el nombre del archivo: ")
    global path_archivo
    path_archivo = path+ f"\\{nombre}.txt"
    try:
        fichero = open(path_archivo, 'w')
        fichero.read
        fichero.close()
    except:
        print("ERROR.")

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

def borrar_archivo():
    try:
        fichero = fichero = open(path_archivo, 'w')
        fichero.close()
    except:
        ("ERROR.")

def leer_lineas():
    try:
        archivo = open(path_archivo,'r')
        while True:
            linea = archivo.readline()
            if linea == "":
                break
            print(linea)
        archivo.close()
    except:
        print("ERROR.")



while True:
    opcion = input(
    """
-----------MENU PRINCIPAL-----------
Por favor ingrese una opcion:
    1. Crear un archivo
    2. Escribir datos
    3. Borrar archivos
    4. Leer archivo
    5. Salir
Numero: """
    )
    if (opcion=="1"):
        crear_archivo()
    elif (opcion=="2"):
        pedir_palabra()
    elif (opcion=="3"):
        borrar_archivo()
    elif (opcion=="4"):
        leer_lineas()
    elif (opcion=="5"):
        print("Gracias por utilizar este programa!")
        break