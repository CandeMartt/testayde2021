"""#### **Ejercicio 7.5 (FALTA)**
Crear una clase para leer archivos (lectorDeArchivos).

Crear funciones para:
*   Leer el archivo e imprimir todo su contenido
*   Encontrar la cantidad de comas en el archivo.
*   Contar la cantidad de palabras de 3 letras y guardarlas en un lista
*   Especificar una palabra a quitar e imprimir el contenido sin esta palabra"""

import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°

class LectorDeArchivo: 
    def leer_archivo(self):
        archivo = input("Ingrese el nombre del archivo a leer con su formato): ")
        path_archivo = path +"\\"+ archivo
        try:
            fichero = open (path_archivo,'r')#fichero = open(path+"\\archivo.txt", 'r')#
            print(fichero.read())
            fichero.close()
        except:
            print("ERROR.")

    def encontar_cant_comas(self):
        archivo = input("Ingrese el nombre del archivo a leer con su formato): ")
        path_archivo = path +"\\"+ archivo
        try:
            fichero = open (path_archivo,'r')#fichero = open(path+"\\archivo.txt", 'r')#
            archivo_texto = fichero.read()
            cont = 0
            for i in archivo_texto:
                if i == ",":
                    cont += 1
            fichero.close()
            print(f"El texto tiene {cont} comas")
        except:
            print("ERROR.")

    def encontrar_cant_comas_2(self):
        archivo = input("Ingrese el nombre del archivo a leer con su formato): ")
        path_archivo = path +"\\"+ archivo
        try:
            fichero = open(path_archivo, 'r')
            cont = 0  
            caracter = fichero.readline(1)
            while caracter != "":
                if (caracter == ","):
                    cont+=1
                caracter = fichero.readline(1)
            fichero.close()
            print(cont)
        except:
                print("no existe el archivo")

    def palabras_tres_letras(self):
        archivo = input("Ingrese el nombre del archivo a leer con su formato): ")
        path_archivo = path +"\\"+ archivo
        try:
            fichero = open(path_archivo,'r')
            texto = fichero.readline()
            lista = texto.split(",")
            acum= 0
            for i in len(lista):
                if i == 3 :
                    acum += i
            print(f"Se encuentran {acum} palabras con tres letras.")
            fichero.close()
        except:
            print("ERROR.")

    def palabra_a_quitar(self):
        archivo = input("Ingrese el nombre del archivo a leer con su formato): ")
        path_archivo = path +"\\"+ archivo 
        try:
            fichero = open(path_archivo, 'r')
            texto = fichero.read()
            lista = texto.split(" ")
            print(lista)
            palabra = input("Ingrese la palabra que desea quitar del texto: ")
            for i in lista:
                if i == palabra:
                    fichero.write(palabra = "")
            print(texto)
            fichero.close()
        except:
            print("ERROR.")

            


    


lector = LectorDeArchivo()
#lector.leer_archivo()
#lector.encontrar_cant_comas_2()
#lector.palabras_tres_letras()
lector.palabra_a_quitar()