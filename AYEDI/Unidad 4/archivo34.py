#02/09/2021
"""
###**Ejercicio 4.3 (Palabras)**
El programa debe:
*   Contar con 3 funciones:
    1. Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o 
    frase (Ambos parametros)
    2. Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.
    IMPORANTE:deben ser palabras y no frases (verificar)
    3. Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y 
    quitar todas las vocales
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""

def contador_de_letras(letra,palabra_o_frase):
    contador = 0
    for i in palabra_o_frase:
        if i == letra:
            contador+=1
    print(f"La palabra {palabra_o_frase} tiene {contador} letras")

def comparador_de_palabras(palabra_1,palabra_2):
    contador_1=0
    contador_2=0
    for i in palabra_1:
        if i!=" ":
            contador_1+=1 
        else:
            contador_1=-1 #si hay espacios es porque es una frase
            break
    for i in palabra_2:
        if i!=" ":
            contador_2+=1 #es una palabra y la acumula
        else:
            contador_2=-1
            break
    if contador_1==-1 or contador_2==-1: #aca se demuestra si es una frase y le avisa al usuario
        return "Se ha ingresado una frase"
    elif contador_1>contador_2:
        return "La palabra 1 tiene más letras"
    elif contador_1 == contador_2:
        return "La palabra tiene la misma cantidad de letras"
    else:
        return "La palabra 2 tiene más letras"

def sin_vocales():
    vocales =("a", "e", "i", "o", "u", "A", "E", "I", "O","U") 
    palabra_frase = str(input("Ingrese una palabra o frase: "))


while True:
      condicion=str(input(
        """Por favor ingrese la opcion que desee utilizar
            1. Contar cantidad e letras
            2. Comparar palabras
            3. Quitar vocales de una palabra o frase
            4. Salir
        Numero: """))
    
      if condicion == "1":   
        while True:
            letra = str(input("Ingrese una letra: "))
            if letra.isalpha():
                if len(letra) == 1: #solo una letra
                    break
        while True:
           palabra = str(input("Ingrese una palabra o frase: "))
           if len(palabra)>3: 
                break
         
        print(f"la cantidad de letras {letra} en {palabra} es: {contador_de_letras(letra,palabra)}")
      elif condicion =="2": 
        try:
            palabra= str(input("Ingrese una palabra: "))
            comparador_de_palabras()
        except:
            print("ERROR. Por favor ingrese solo una palabra")

      elif condicion =="3": 
        try:
            palabra_frase = str(input("Ingrese una palabra o frase: "))   
            sin_vocales()
        except:
            print("ERROR. Por favor ingrese una palabra o frase")

      elif condicion =="4":   
            print("Gracias por utilizar este programa! Hasta luego!")
            break
      else:
          print("No ingreso una opcion correcta")

