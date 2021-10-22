lista_persona = []
import Persona as pn
def crar_personas():
    while True: #pide DNI
        dni = input("Por favor ingrese el DNI de la persona: ")
        if dni.isdigit():
            flag_agregar = True
            for persona in lista_persona:
                if dni  == persona.dni:
                    print("Ese DNI ya existe")
                    flag_agregar = False
                    break
            if(flag_agregar): #significa que el DNI es valido, puede salir del while
                break
        else:
            print("El DNI debe se numerico")
    #nombre
    while True:
        nombre = input("Por favor ingrese el nombre de la persona: ").capitalize()
        if not nombre.isalpha():
            print("Un nombre no puede tener simbolos.")
        else:
            break
    #apellido
    while True:
        apellido = input("Por favor ingrese el apellido de la persona: ").capitalize()
        if not apellido.isalpha():
            print("Un nombre no puede tener simbolos.")
        else:
            break
    #edad
    while True:
        try:
            edad = int(input("Por favor ingrese la edad de la persona: "))
            if edad <=0:
                print("La edad debe ser mayor de cero")
            else:
                break
        except:
            print("ERROR.")

   #residencia
    residencia = input("Por favor ingrese la residencia de la persona: ").capitalize()
    nombre_instancia = dni + nombre
    #instanciando o creando un objeto de persona
    nombre_instancia = pn.Persona(dni,nombre,apellido,edad,residencia)
    lista_persona.append(nombre_instancia)

def listar_personas():
    for persona in lista_persona:
        persona.presentarse()

def consultar_rango():
    print("------ LISTA DE PERSONAS ------")
    for persona in lista_persona:
        print(f"{persona.dni} \t {persona.nombre} \t{persona.apellido} \t {persona.edad} \t {persona.residencia} ")
        while True: #pide DNI
            dni_consultar = input("Por favor ingrese el DNI de la persona: ")
            if dni_consultar.isdigit():
                for persona in lista_persona:
                    if dni_consultar  == persona.dni:
                        persona.rando_edad()
                        return
            else:
                print("El DNI debe se numerico")