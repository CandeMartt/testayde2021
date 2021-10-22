import Autos as au
lista_autos = []

def crar_auto():
    while True: 
        codigo = input("Por favor ingrese el código del auto: ")
        if codigo.isdigit():
            flag_agregar = True
            for auto in lista_autos:
                if codigo  == auto.codigo:
                    print("Ese código ya existe")
                    flag_agregar = False
                    break
            if(flag_agregar):
                break
        else:
            print("El código del auto debe ser numérico")
            
    #nombre del auto
    nombre_auto = input("Por favor ingrese el nombre del auto (por ejemplo: auto_1): ")

    #color del auto
    while True:
        color = input("Por favor ingrese el color del auto: ")
        if not color.isalpha():
            print("El color no debe tener simbolos ni numeros")
        else:
            break

    #marca del auto
    while True:
        marca = input("Por favor ingrese la marca del auto: ").capitalize()
        if not marca.isalpha():
            print("La marca no puede tener simbolos.")
        else:
            break

    #cantidad de puertas
    while True:
        try:
            puertas = int(input("Por favor ingrese la cantidad de puertas que tiene el auto: "))
            if puertas <=0:
                print("La cantidad de puertas debe ser mayor de cero")
            else:
                break
        except:
            print("ERROR.")

    nombre_instancia = codigo + nombre_auto
    #instanciando o creando un objeto de persona
    nombre_instancia = au.Autos(codigo, nombre_auto, color, marca, puertas)
    lista_autos.append(nombre_instancia)

def tabla_lista():
    print("------ LISTA DE AUTOS ------")
    print("Código \t Auto \t \t Color \t Marca \t Cantidad de puertas" )
    for auto in lista_autos:
        print(f"{auto.codigo} \t {auto.nombre_auto} \t{auto.color} \t {auto.marca} \t {auto.puertas} ")

def listar_autos():
    for auto in lista_autos:
        auto.presentar_auto()