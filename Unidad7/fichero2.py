"""
#### **Ejercicio 7.2**
Crear una funcion para leer el un archivo.txt.
*   pedir al usuario una palabra y encontrar la cantidad de 
veces que aparece esa palabra en el archivo
"""
try:
    fichero = open ("archivo2,txt",'r')
    palabra = input("Ingrese la palabra que desea buscar: ")
    texto = fichero.read()
    lista = texto.split()
    acum= 0
    for i in lista:
        if i == palabra:
            acum += i
    print(f"La palabra {palabra} se encuentran {acum}")
    fichero.close()
except:
    print("no existe el archivo")

"""
try:
    fichero = open ("archivo2.txt",'r')
    palabra_buscada=input("Ingrese una palabra: ")
    texto=fichero.read()
    lista=texto.split()
    cont=0
    for palabra in lista:
        if palabra==palabra_buscada:
            cont+=1
    print(f"La palabra se encuentra {cont} veces en el Archivo.")
    fichero.close()
except:
        print("no existe el archivo")
"""