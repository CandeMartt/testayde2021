def recorrido_viaje(Taxis):
    try:
        recorrido = int(input("Por favor ingrese cual el recorrido máximo de su viaje: "))
        if(recorrido <= 0):
            print("La distancia debe ser mayor que cero")
        else:
            print("Posibles autos que podrían realizar el viaje:")
            for i in range(len(Taxis[2])):
                if(recorrido <= Taxis[2][i]):
                    print(f"Auto: {Taxis[0][i]} - Chofer: {Taxis[1][i]}")
    except:
        print("ERROR.")
    return Taxis
                

def nombre_chofer(Taxis):
    while True:
        choferes_recorridos(Taxis)
        indicar_auto = input("Nombre del auto a modificar: ")
        nombre = input("Ingrese el nuevo nombre del chofer: ")
        if indicar_auto in Taxis[0]:
           Taxis[1][Taxis[0].index(indicar_auto)]= nombre
           print(f"El nombre del chofer del Auto 1 es {Taxis[1][Taxis[0].index(indicar_auto)]}")
           choferes_recorridos(Taxis)
           break
        else:
            print("Este auto no trabaja en esta empresa")
    return Taxis

    
def modificar_recorrido(Taxis):
  while True:
    choferes_recorridos(Taxis)
    indicar_auto = input("Nombre del auto a modificar: ")
    recorrido_nuevo = input("Ingrese el nuevo recorrido: ")
    if indicar_auto in Taxis[0]:
        Taxis[2][Taxis[0].index(indicar_auto)]= recorrido_nuevo
        print(f"El nuevo recorrido de {indicar_auto} es {Taxis[2][Taxis[0].index(indicar_auto)]}")
        choferes_recorridos(Taxis)
        break
    else:
        print("Este auto no trabaja en esta empresa")
    return Taxis

def nuevo_trabajador(Taxis):
    while True:
        nuevo_auto = input("Por favor ingrese un nuevo auto: ")
        Taxis[0].append(nuevo_auto)
        nuevo_chofer = input("Por favor ingrese el nombre del nuevo chofer: ")
        if nuevo_chofer.isalpha():
            Taxis[1].append(nuevo_chofer)
        else:
            print("Por favor ingrese un nombre que no contenga numeros ni caracteres.")
        nuevo_recorrido = int(input("Por favor ingrese el recorrido máximo que hará: "))
        Taxis[2].append(nuevo_recorrido)
        print({f"{Taxis}"})
        break
    return Taxis


def choferes_recorridos(Taxis):
    print("  AUTO  -  CHOFER  - RECORRIDO MÁX.")
    for i in range(len(Taxis[0])):
        print(f"{Taxis[0][i]} - {Taxis[1][i]} - {Taxis[2][i]}")
        

def informacion_chofer(Taxis):
    while True:
        chofer = input("Por favor ingrese el nombre del chofer: ")
        if chofer.isalpha():
            if chofer in Taxis[1]:
                print (f"{chofer} maneja el {Taxis[0][Taxis[1].index(chofer)]} y hace {Taxis[2][Taxis[1].index(chofer)]} kilómetros.")
                break
            else:
                print("Este chofer no trabaja en esta empresa")
    return Taxis







