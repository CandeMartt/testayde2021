"""
*   Se debe crear una clase GestorEvento que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de un evento y guárdalos en una lista de eventos. 
        1.1) Se debe verificar que tipo de instancia de evento a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - nombre_evento: debe ser único
             - Fecha: formato (dd/mm/yyyy) -> únicamente verificar la longitud del string = 10 
             - Hora: formato (hh:mm) -> no es necesario verificar
             - Lugar: sin formato especifico, no es necesario verificar
        1.2) Al crear un evento es necesario logearlo (Escribir en una línea nueva: nombre_evento-Fecha-Hora-Lugar-Tipo_de_evento(tipo de clase)) 
             en un archivo llamado lista_eventos.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos
        1.3) En caso que la instancia del evento sea EventoPersonal.
             - Para el organizador, el usuario debe elegir a través de una clave (mostradas por el programa) 
                desde un diccionario de organizadores.
             - En caso que no exista el organizador deseado debe ser "incognito" (AYUDA: Funcion get de diccionarios)
    2.   Listar eventos disponibles, leyendo la lista_evetos.txt. IMPORTANTE!: recorrer el archivo, no la lista. 
    3.   Cambiar el lugar de un evento, seleccionando su nombre. (Hacer check correspondientes)
    
*   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
organizadores = {
    "FA":"familia", 
    "AM": "amigos",
    "PR": "propio"
    }
"""

import Evento as ev
lista_eventos = []


class GestorEvento:
    def crear_evento(self):
        while True:
            condicion=input(
            """
        ---------------- CREAR EVENTO ----------------
        Por favor ingrese la opcion que desee utilizar
            1. Evento Genérico
            2. Evento Personal
            3. Evento Laboral
        Número: """)

            if condicion == "1" or condicion == "2" or condicion == "3":
                break
            else:
                print("Opcion incorrecta")

     #self, nombre_evento, fecha, hora, lugar   
        while True: #pide nombre evento (ÚNICO)
            nombre_evento = input("Ingrese el nombre del evento: ")
            flag_agregar = True
            for i in lista_eventos:
                if (nombre_evento == i.get_nombre_evento()):
                    print("El evento debe ser único")
                    flag_agregar = False
                    break
            if(flag_agregar): #significa que el evento es valido, puede salir del while
                break

        fecha = input("Ingrese la fecha del evento: ")
        if len(fecha) == 10:
           pass
        else:
            print("La fecha del evento debe ser (dd/mm/yyyy)")
             
        hora = input("Ingrese la hora del evento: ")
        lugar = input("Ingrese el lugar del evento: ")

#Agrega el atributo "organizador"
        if condicion == "2":
          organizadores = {
            "FA":"familia", 
            "AM": "amigos",
            "PR": "propio"
            }
          print("""
               ---------------- ORGANIZADOR ----------------
                            "FA":"familia", 
                            "AM": "amigos",
                            "PR": "propio"

               """)
          organizador = input("Ingrese el organizador que desea:  ")
          valor = organizadores.get(organizador, "INCOGNITO")
          print(f"La opción {organizador} corresponde a {valor}.")


#Agrega el atributo "obligatorio"
        if condicion == "3":
           obligatorio = input("Ingrese True si es obligatorio y False si no es obligatorio: ")
           
        if condicion == "1":
            nombre_instancia = ev.Evento(nombre_evento, fecha, hora, lugar)
        elif condicion == "2":
            nombre_instancia = ev.EventoPersonal(nombre_evento, fecha, hora, lugar, organizador)
        elif condicion == "3":
            nombre_instancia = ev.EventoLaboral(nombre_evento, fecha, hora, lugar, obligatorio)
        
        lista_eventos.append(nombre_instancia)

#nombre_evento-Fecha-Hora-Lugar-Tipo_de_evento(tipo de clase)
        import os
        path = os.path.abspath(os.path.dirname(__file__))
        path_archivo = path+"\\lista_eventos.txt"
        try:
            fichero = open(path_archivo, 'a+')
            fichero.write(f"Nombre del evento: {nombre_evento}, Fecha: {fecha}, Hora: {hora}, Lugar: {lugar} \n")
            fichero.close()
        except:
            print("ERROR.")
            
#Imprime la lista de los eventos del archivo txt
    def listar_eventos_disponibles(self):
        import os
        path = os.path.abspath(os.path.dirname(__file__))
        path_archivo = path+"\\lista_eventos.txt"
        try:
            fichero = open (path_archivo,'r')
            print(fichero.read())
            fichero.close()
        except:
            print("ERROR.")

    def imprimir_eventos(self):
        for i in lista_eventos:
            i.presentarse()
            i.tipo_objeto()

#Cambia el lugar del evento
    def cambiar_lugar(self):
            if len(lista_eventos) == 0: #Me aseguro que la lista no este vacia al iniciar 
                    print("La lista de eventos esta vacia. Por favor agregue eventos. ")
            flag_principal = True #Me aseguro de romper el primer while al agregar este flag.
            while flag_principal: #En este while compuebo que el nombre del evento exista
                nom_evento = input("Ingrese el nombre del evento: ")
                flag = True
                for i in lista_eventos:
                    if nom_evento == i.get_nombre_evento():
                        flag = False
                if flag == False:
                    print("Valido")
                    print(i.get_nombre_evento()) 
                    flag_principal = False
                else:
                    print("Evento invalido")    

            nuevo_lugar = input("Ingrese el nuevo lugar del evento: ")
            i.set_lugar(nuevo_lugar) #Esto no me lo estaría tomando profe. 
                                     #Me valida el nombre del evento UNICO pero no me hace el cambio de lugar :(


            



        
