#05/05/2022
"""
Ejercicio 3.1
Crear una clase padre Colegio:

Crear metodos para esta clase de:
    1- Constructor con: nombre, año, direccion
    2- seters y gettes
    3- get_clase (que clase es) 

Crear una clase padre Club:
Crear metodos para esta clase de:
    1- Constructor con: nombre, año, direccion
    2- seters y gettes
    3- get_clase (que clase es)

Crear una clase Organizacion que herede de Colegio y Club:

Crear un menu con las funciones de

Crear Colegio, club o organizacion y guardar en una lista
Listar
"""
class Colegio:
    def __init__(self, nombre, año, direccion ):
        self.nombre = nombre
        self.año = año
        self.direccion = direccion

    def get_nombre(self): 
        return (f"{self.nombre}")

    def get_año(self): 
        return (f"{self.año}")

    def get_direccion(self): 
        return (f"{self.direccion}")

    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_año(self,nuevo_año):
        self.año = nuevo_año

    def set_direccion(self,nueva_direccion):
        self.nombre = nueva_direccion

    def get_clase(self):
        print("Soy la clase: ", type(self).__name_)

class Club:
    def __init__(self, nombre, año, direccion ):
        self.nombre = nombre
        self.año = año
        self.direccion = direccion

    def get_nombre(self): 
        return (f"{self.nombre}")

    def get_año(self): 
        return (f"{self.año}")

    def get_direccion(self): 
        return (f"{self.direccion}")

    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_año(self,nuevo_año):
        self.año = nuevo_año

    def set_direccion(self,nueva_direccion):
        self.nombre = nueva_direccion
        
    def get_clase(self):
        print("Soy la clase: ", type(self).__name_)

class Organizacion(Colegio,Club):
    def __init__(self, nombre, año, direccion):
        super().__init__(nombre,año, direccion)
