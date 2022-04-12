"""
Contar con una Clase Persona con los atributos (dni (int - único), nombre (string), apellido (string))
Contar con una Clase Hija Empleado que use el constructor de la clase padre con los atributos:
funcion (string)
año_ingreso (string 'yyyy')
Se deben crear los siguientes métodos para la clase padre Persona (que heredará la clase hija):
Set y Get dni.
Se deben crear los siguientes métodos para la clase hija.

*  Set y Get funcion.
Se debe contar y crear funciones para un menu que tenga las siguiente opciones,
"""
class Persona:
    def __init__(self, dni, nombre ,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def get_dni(self):
        return self.dni
    def set_dni(self, nuevo_dni):
        self.dni = nuevo_dni
        print(f"El nuevo dni es {nuevo_dni}")
        
class Empleado(Persona):
    def __init__(self, dni, nombre ,apellido, funcion, año_ingreso):
        super().__init__(dni, nombre ,apellido)
        self.funcion = funcion
        self.año_ingreso =año_ingreso

    def get_funcion(self):
        return self.funcion

    def set_funcion(self, nueva_funcion):
        self.funcion = nueva_funcion
        print(f"El nueva funcion es {nueva_funcion}")

    def imprimir_info_empleados(self):
        print(f"Empleado: {self.nombre} {self.apellido} - DNI: {self.dni} - Funcion: {self.funcion} - Año de ingreso {self.año_ingreso} ")

    def __repr__(self): 
        #especifico el orden de los atributos en el objeto para el SORTED
        #MUY IMPORTANTE! sin esto no encuentra el objeto!!
        return "Empleado ({}-{}-{}-{}-{})".format(self.dni, self.nombre, self.apellido, self.funcion, self.año_ingreso) #Tienen que estar TODOS los atributos, sino no funciona