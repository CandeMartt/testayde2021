"""
#### **Ejercicio 7.1**
Crear una funcion para leer el un archivo.txt hasta encontrar un punto.
"""
try:
    fichero = open ("archivo.txt",'r')#fichero = open(path+"\\archivo.txt", 'r')#
    print(fichero.read())
    fichero.close()
except:
    print("no existe el archivo")