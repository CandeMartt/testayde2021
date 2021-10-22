def alfabeto (alfabeto_a):
    print("-----------------------------------ALFABETO-----------------------------------")
    print(f"{alfabeto_a}")
    return


def alfabeto_moorse (alfabeto_b):
    print("------------------------------ALFABETO EN CÓDIGO MORSE------------------------------")
    print(f"{alfabeto_b}")
    return

def modificar_letras(alfabeto_a,alfabeto_b):
    try:
        letra_modificar = str(input("Ingrese la letra que desea modificar: "))
        nueva_letra = str(input("Ingrese la nueva letra por la que desee cambiarla: "))
        if letra_modificar in alfabeto_a:
            alfabeto_a[alfabeto_a.index(letra_modificar)] = nueva_letra
            letra_modificar_b = str(input("Ingrese la misma letra que modificó anteriormente pero en moorse: "))
            if letra_modificar_b in alfabeto_b:
                nueva_letra_b = str(input("Ingrese la nueva letra para el alfabeto en código moorse: "))
                alfabeto_b[alfabeto_b.index(letra_modificar_b)] = nueva_letra_b
        elif letra_modificar in alfabeto_b:
            alfabeto_b[alfabeto_b.index(letra_modificar)] = nueva_letra
            letra_modificar_a = str(input("Ingrese la misma letra que modificó anteriormente pero en abc: "))
            if letra_modificar_a in alfabeto_a:
                nueva_letra_a = str(input("Ingrese la nueva letra para el alfabeto abc: "))
                alfabeto_a[alfabeto_a.index(letra_modificar_a)] = nueva_letra_a
    except:
        print("ERROR.")
    print(f"{alfabeto_a, alfabeto_b}")
    return alfabeto_a, alfabeto_b

def convertir_alfabeto_A(alfabeto_a, alfabeto_b):
    try:
        alfabeto_a = alfabeto_b
    except:
        print("ERROR.")
    print(f"{alfabeto_a}")
    return alfabeto_a, alfabeto_b

def convertir_alfabeto_B(alfabeto_a, alfabeto_b):
    try:
        alfabeto_b = alfabeto_a
    except:
        print("ERROR.")
    print(f"{alfabeto_b}")
    return alfabeto_a, alfabeto_b

def verificar_letras_a(alfabeto_a):
    letra_verificar = input("Ingrese la letra que desea verificar del alfabeto abc: ")
    if letra_verificar in alfabeto_a:
        print(f"La letra {letra_verificar} se encuentra en el alfabeto.")
    else:
        print(f"La letra {letra_verificar} no se encuentra en el alfabeto")
  

def verificar_letras_b(alfabeto_b):
    letra_verificar = input("Ingrese la letra que desee verificar del Código Moorse: ")
    if letra_verificar in alfabeto_b:
       print(f"La letra {letra_verificar} se encuentra en el alfabeto Moorse.")
    else:
       print(f"La letra {letra_verificar} no se encuentra en el alfabeto Moorse")
   
def convertir_alfabeto_aa (alfabeto_a, alfabeto_b):
    letra = input("Ingrese la letra que desea convertir: ")
    if letra in alfabeto_a:
        alfabeto_a[alfabeto_a.index(letra)] = alfabeto_b[alfabeto_a.index(letra)]
        print(f"{alfabeto_a,alfabeto_b}")
    elif letra in alfabeto_b:
        alfabeto_b[alfabeto_b.index(letra)] = alfabeto_a[alfabeto_b.index(letra)]
        print(f"{alfabeto_a,alfabeto_b}")
        
        


alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]

convertir_alfabeto_aa(alfabeto_a, alfabeto_b)