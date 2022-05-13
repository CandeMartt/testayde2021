"""
###**Ejercicio 3.6**
Crear una clase Persona con metodos estaticos, de clase y de instancia.
- Tiene que tener un atributo de clase: Nacionalidad

Los metodos a crear son:
- Conctructor con atributos DNI, nombre, apellido
-  **Metodos de clase:** set y get nacionalidad
-  **Metodos de intancia:** setters y getters, crear con @propierty
-  **Metodos estaticos:** ejercicio anterior

Crear un menu para probar todos los requerimientos
"""
from datetime import date, time, datetime
class Persona():
    nacionalidad = "ARGENTINA"
    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    @classmethod
    def set_nacionalidad(cls,x):
        cls.nacionalidad = x
    @classmethod
    def get_nacionalidad (cls):
        return cls.nacionalidad

    @property 
    def dni(self): #get
        return self.dni
    @dni.setter
    def dni(self,nuevo_dni): #set
        self.dni = nuevo_dni
 
    @property
    def nombre(self): #get
        return self.nombre
    @nombre.setter
    def nombre(self,nuevo_nombre): #set
        self.nombre = nuevo_nombre

    @property
    def apellido(self): #get
        return self.apellido
    @apellido.setter
    def apellido(self,nuevo_apellido): #set
        self.apellido = nuevo_apellido
    

    @staticmethod
    def calcular_IMC(peso,estatura):
        return peso/(estatura/100)**2
    
    @staticmethod
    def calcular_edad (fecha_nacimiento):
        now = datetime.now()
        date = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
        return (now-date)/365