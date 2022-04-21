lista_empleados = []
import clases as cl
from datetime import date, time, datetime

class gestorPersonas:
    def crear_empleado(self):
        #DNI
        while True:
            dni = input("Por favor ingrese el DNI del empleado: ")
            if dni.isdigit():
                flag_agregar = True
                for empleado in lista_empleados:
                    if dni  == empleado.dni:
                        print("Ese DNI ya existe")
                        flag_agregar = False
                        break
                if(flag_agregar): #significa que el DNI es valido, puede salir del while
                    break
            else:
                print("El DNI debe se numerico (SIN PUNTOS,NI ESPACIOS).")
        #Nombre
        nombre = input("Ingrese el nombre del empleado: ").capitalize()

        #Apellido 
        apellido = input("Ingrese el apellido del empleado: ").capitalize()

        #Funcion
        funcion = input("Ingrese la funcion del empleado: ").capitalize()

        #Año ingreso
        while True:
            try:
                fecha_ingresada = datetime.strptime(input("Ingrese el año de ingreso del empleado dd/mm/yyyy : "),
                                                    '%d/%m/%Y')
                break
            except:
                print('Fecha mal ingresada')
       
        nombre_instancia = cl.Empleado(dni,nombre, apellido, funcion, fecha_ingresada)
        lista_empleados.append(nombre_instancia)
    
    def imprimir_info_empleados(self):
        for i in lista_empleados:
            i.imprimir_info_empleados()
    
    
    def ordenar_por_fecha_me_a_mayor(self):
        lista_aux_ordenada = []
        global lista_empleados #habia que declarar la lista como global para obtener elementos
        while( len(lista_empleados)>0):
            objeto_menor = lista_empleados[0]
            for empleado in lista_empleados:
                if (empleado.get_fecha() < objeto_menor.get_fecha()):
                    objeto_menor = empleado
            
            lista_aux_ordenada.append(objeto_menor)#agrego el menor a la lista
            lista_empleados.remove(objeto_menor)
        
        lista_empleados = lista_aux_ordenada
        self.imprimir_info_empleados()