#25/08/2021

"""
El programa debe
-El usuario debe ingresar un numero inicial
-El usuario debe ingresar un numero limite
-Imprimir todos los numeros del numero inicial al limite
-No debe generar error
"""
flag = True
while flag:
    try:
        numero_inicial = int(input("Ingrese numero inicial "))
        numero_limite = int(input("Ingrese numero limite "))

        if(numero_inicial<numero_limite):
            while numero_inicial<= numero_limite:
                print(numero_inicial)
                numero_inicial+=1
                flag = False
        else:
                    print("El numero inicial debe ser menor que el limite")
    except: 
        print("Ingrese un numero.")
 