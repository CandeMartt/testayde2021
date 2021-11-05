import os
from posixpath import split
#path actual
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
path_tabla = path+"\\archivo.csv"
print(path+"\\archivo.csv")##\\ por caracteres especiales

def leer_titulos():
    try:
        tabla = open(path_tabla,'r')
        titulos = tabla.readline()
        lista_titulos = titulos.split(',')
        print("Los titulos son: ", end="")
        acum = 0
        for i in lista_titulos:
            print(i,end = "-") 
            acum += 1
        print(f"La cantidad de columnas son {acum}") 
        tabla.close()
    except:
        print("ERROR.")

leer_titulos()

def leer_lineas():
    try:
        tabla = open(path_tabla,'r')
        cont = 0
        while True:
            fila = tabla.readline()
            if fila == "":
                break
            cont += 1
        print(f"La cantidad de filas son {cont}")
        tabla.close()
    except:
        print("ERROR.")

leer_lineas()

