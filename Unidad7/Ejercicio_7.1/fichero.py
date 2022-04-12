"""
#### **Ejercicio 7.1**
Crear una funcion para leer el un archivo.txt hasta encontrar un punto.
"""
try:
    fichero = open("archivo1.txt",'r')
    while True:
        caracter = fichero.readline(1)
        print(caracter, end="")
        if (caracter == "."):
            break 
    fichero.close
except:
    print("no existe el archivo")