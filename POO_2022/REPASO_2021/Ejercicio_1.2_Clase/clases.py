"""
Contar con:
 *  Contar con una Clase **Persona** con los atributos (dni (int - único), nombre (string), apellido (string))
 *  Contar con una Clase Hija **Empleado** que use el constructor de la clase padre con los atributos:
  -  **funcion** (string)
  -  **año_ingreso** (string 'yyyy')
 *  Se deben crear los siguientes métodos para la clase padre Persona (que heredará la clase hija):
  *  Set y Get dni.

Se deben crear los siguientes métodos para la clase hija.
    
    *  Set y Get funcion.
    
"""
class Persona:
    def __init__(self,dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apellido = apellido
    
    def set_dni(self,dni_nuevo):
        self.dni = dni_nuevo
    
    def get_dni(self):
        return self.dni

class Empleado(Persona):
    def __init__(self,dni,nombre,apellido,funcion,fecha_ingreso):
        super().__init__(dni,nombre,apellido)
        self.funcion = funcion
        self.fecha_ingreso = fecha_ingreso
    
    def set_funcion(self,funcion_nueva):
        self.funcion = funcion_nueva
    
    def get_funcion(self):
        return self.funcion
    
    def get_fecha(self):
        return self.fecha_ingreso

    def imprimir_info_empleados(self):
        print(f" DNI: {self.dni} - Empleado: {self.nombre} {self.apellido} - Funcion: {self.funcion} - Año de ingreso {self.fecha_ingreso} ")