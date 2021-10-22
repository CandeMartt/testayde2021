"""##**Ejercicio 5.7 (Estadisiticas)**
El programa debe:
*   Simular un programa que calcule estadisticas
*   Pedir al usuario una serie de numeros enteros el 1 al 10 (verificar) y guardarlos en una lista, hasta que el usuario ingrese "fin"
*   Luego mostrar un menu con 4 opciones
  1.  Calcular promedio
  2.  Verificar cuantos numeros son menores que el numero indicado por el usuario
  3.  Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
  4.  Verificar si un numero que desee el usuario esta en la lista
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio"""

def pedido_numeros():
    lista_numeros = []
    contador = 1
    while True:
        entrada = input(f"Ingrese el {contador}º numero (entre el 1 y el 10) o fin: ")
        if entrada == "fin":
            break
        else: 
            try:
                if int(entrada) > 0 and int(entrada)<=10:
                    lista_numeros.append(int(entrada))
                    contador += 1
                else: 
                    print("Dato incorrecto!")
            except: 
                print("ERROR.")

    return lista_numeros

def promedios(lista_principal):
    suma_total = sum(lista_principal)
    total_numero = len(lista_principal)
    return round(suma_total/total_numero,2)

def cant_numeros_menores(lista_principal):
    while True:
        try:
            numero_comparar = int(input("Ingrese el numero a comparar "))
            break
        except:
            print("Por favor ingrese un numero")
    contador = 0
    for i in lista_principal:
        if i < numero_comparar:
            contador += 1

    return contador

def cant_numeros_mayores(lista_principal):
    while True:
        try:
            numero_comparar = int(input("Ingrese el numero a comparar: "))
            break
        except:
            print("Por favor ingrese un numero")
    contador = 0
    for i in lista_principal:
        if i >= numero_comparar:
            contador += 1

    return contador

def igual_numero(lista_principal): #cuantas veces esta
    while True:
        try:
            numero_deseado = int(input("Ingrese un numero deseado: "))
            break
        except:
            print("Por favor ingrese un numero")
    contador = 0
    for i in lista_principal:
        if i == numero_deseado:
             contador += 1

    return contador

def numero_en_lista(lista_principal): #si esta o no
    while True:
        try:
            numero_comparar = int(input("Indique el numero a buscar: "))
            break
        except:
            print("Dato Incorrecto!")
    
    if numero_comparar in lista_principal: #busca si directamente
        contador=True
    else:
        contador=False
    return contador

while True:
        condicion=input(
            """Por favor ingrese la opcion que desee utilizar
                1. Calcular promedio
                2. Identificar números menores al ingresado
                3. Identificar números mayores o igual al ingresado
                4. Verificar si el número ingresa ya esta en la lista
                5. Salir
            Numero: """)
        
        if condicion == "1": 
            lista_principal = pedido_numeros()
            print(lista_principal)
            promedios(lista_principal)
            print(f"El promedio de la lista es {promedios(lista_principal)}")
        elif condicion =="2": 
            lista_principal = pedido_numeros()
            print(lista_principal)
            cant_numeros_menores(lista_principal)
            print(f"Los numeros menores son: {cant_numeros_menores(lista_principal)}")
        elif condicion =="3": 
            lista_principal = pedido_numeros()
            print(lista_principal)
            cant_numeros_mayores(lista_principal)
            print(f"Los numeros mayores o iguales son: {cant_numeros_mayores(lista_principal)}")
        elif condicion == "4":
            lista_principal = pedido_numeros()
            print(lista_principal)
            igual_numero(lista_principal)
            numero_en_lista(lista_principal)
            print(f"El número que usted ingresó {numero_en_lista(lista_principal)} en en la lista.\n \
            Se encuentan repetidos {igual_numero(lista_principal)} vez/veces en la lista.")
        elif condicion =="5":   
                print("Gracias por utilizar este programa! Hasta luego!")
                break
        else:
            print("No ingreso una opcion correcta")







       