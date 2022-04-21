"""
Crear un empleado y guardarlo en una lista_empleados
Recorrer la lista de empleados segun DNI, mayor a menor o menor a mayor
Recorrer la lista de empleados segun fecha_ingreso, mayor a menor o menor a mayor
Eliminar el ultimo empleado agregado
"""
lista_empleados = []
import Persona as pn

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
        año_ingreso = int(input("Ingrese el año de ingreso del empleado: "))

        nombre_instancia = pn.Empleado(dni,nombre, apellido, funcion, año_ingreso)
        lista_empleados.append(nombre_instancia)


    def imprimir_info_empleados(self):
        for i in lista_empleados:
            i.imprimir_info_empleados()

    def imprimir_por_dni(self): #SORTED: Acomoda la lista de empleados por DNI de MENOR A MAYOR
        print(sorted(lista_empleados, key=lambda empleado: empleado.dni)) #.dni = estoy indicandole por cual atributo quiero que me acomode

    def imprimir_por_dni_mayor_a_menor(self): #SORTED-REVERSE: Acomoda la lista de empleados por DNI de MAYOR A MENOR
        print(sorted(lista_empleados, reverse=True, key=lambda empleado: empleado.dni)) #.dni = estoy indicandole por cual atributo quiero que me acomode
        
    def imprimir_por_fecha_de_ingreso(self): #SORTED: Acomoda la lista de empleados por FECHA DE INGRESO de MENOR A MAYOR
        print(sorted(lista_empleados, key=lambda empleado: empleado.año_ingreso)) #.año_ingreso = estoy indicandole por cual atributo quiero que me acomode

    def imprimir_por_fecha_de_ingreso_2(self): #SORTED-REVERSE: Acomoda la lista de empleados por DNI de MAYOR A MENOR
        print(sorted(lista_empleados, reverse=True, key=lambda empleado: empleado.año_ingreso)) #.dni = estoy indicandole por cual atributo quiero que me acomode

    def eliminar_ultimo_empleado(self):
        for i in range(len(lista_empleados)):
            if i == (len(lista_empleados)-1):
                lista_empleados.pop(len(lista_empleados)-1)
        print("Se elimino el ultimo empleado.")