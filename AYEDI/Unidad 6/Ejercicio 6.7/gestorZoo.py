"""
2. Crear instancia de Empleados y guardarlos en una lista
        * Los empleados se les pueden asignar animales luego, los animales al crearlos en el sistema tienen q contar si o si con un encargado
1. Crear instancias de animales (se puede elegir entre los tres sectores)  y guardarlos en una lista
3. Asignar a un empleado un animal a cuidar
4. Cambiar de encargado un animal
5. imprmir lista de animales (con toda su informacions)
6. imprimir lista de Empleados (con toda su informacions)
"""
import Empleados as em
import Animal as an
lista_empleados = []
lista_animales = []
lista_animales_a_cuidar = []

class GestorZoo:
    def crear_instancia_empleado(self):
        while True: #pide legajo
            legajo = input("Ingrese el legajo de la persona: ")
            if legajo.isdigit():
                flag_agregar = True
                for i in lista_empleados:
                    if (legajo == i.get_legajo()):
                        print("El legajo debe ser único")
                        flag_agregar = False
                        break
                if(flag_agregar): #significa que el legajo es valido, puede salir del while
                    break
            else:
                print("El legajo debe se numerico")

        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        nombre_instancia = em.Empleados(legajo,nombre,apellido, lista_animales_a_cuidar)
        lista_empleados.append(nombre_instancia)
        
    
    def imprimir_empleados(self):
        for i in lista_empleados:
            i.presentarse()

    def crear_intancia_animales(self):
        #self, nombre, tipo_animal, fecha_nacimiento, encargado_cuidar
        while True:
            condicion=input(
            """
        ---------------- AGREGAR ANIMAL ----------------
        Por favor ingrese la opcion que desee utilizar:
            1. Animal Genérico
            2. Animal Enjaulado
            3. Animal Suelto
            4. Animal Acuático
        Numero: """)

            if condicion == "1" or condicion == "2" or condicion == "3" or condicion ==  "4":
                break
            else:
                print("Opcion incorrecta")

        self.imprimir_empleados()
        while True:
            encargado_num= input("Ingrese el numero de legajo del encargado de cuidar a este animal: ")
            if encargado_num.isdigit():
                flag = True
                for i in lista_empleados:
                    if encargado_num != i.get_legajo():
                        print("El legajo no existe")
                        flag = False
                    else:
                        if encargado_num == i.get_legajo():
                            encargado_cuidar = i.get_legajo()
                            print("Legajo valido") 
                            break
                if flag:
                    break
                break    
            else:
                print("El legajo debe se numerico")
                

        nombre = input("Ingrese el nombre del animal: ")
        tipo_animal = input("Ingrese el tipo de animal: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del animal: ")

        if condicion == "1":
            nombre_instancia = an.Animal(nombre,tipo_animal,fecha_nacimiento,encargado_cuidar)
        elif condicion == "2":
            nombre_instancia = an.AnimalesEnjaulados(nombre,tipo_animal,fecha_nacimiento,encargado_cuidar)
        elif condicion == "3":
            nombre_instancia = an.AnimalesSueltos(nombre,tipo_animal,fecha_nacimiento,encargado_cuidar)
        
        if condicion == "4":
            nombre_instancia = an.AnimalesAcuaticos(nombre,tipo_animal,fecha_nacimiento,encargado_cuidar)

        lista_animales.append(nombre_instancia)
        lista_animales_a_cuidar.append(nombre_instancia)

    def imprimir_animales(self):
        for i in lista_animales:
            i.presentar_animal()
            i.tipo_objeto()



        
        