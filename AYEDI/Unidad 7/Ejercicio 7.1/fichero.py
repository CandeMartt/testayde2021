import os
#path actual
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
path_archivo = path+"\\archivo.txt"
print(path+"\\archivo.txt")##\\ por caracteres especiales

try:
    fichero = open(path_archivo,'r')
    while True:
        caracter = fichero.readline(1)
        print(caracter, end="")
        if (caracter == "."):
            break 
    fichero.close
except:
    print("no existe el archivo")