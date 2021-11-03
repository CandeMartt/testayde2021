"""
*   La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento, encargado_cuidar (Legajo de objeto empleado))
    *   Crear 3 clases que hereden de animal segun su sector del zoologico)
        1. AnimalesEnjaulados.
        2. AnimalesSueltos.
        3. AnimalesAcuaticos
"""
class Animal:
    #CONSTRUCTOR
    def __init__(self, nombre, tipo_animal, fecha_nacimiento, encargado_cuidar):
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.encargado_cuidar = encargado_cuidar

    def tipo_objeto(self):
        print("Animal tipo", type(self).__name__)

    def set_empleado(self,encargado_cuidar):
        self.encargado_cuidar = encargado_cuidar

    def presentar_animal(self):
        print(f"Nombre: {self.nombre}, Tpo de anima {self.tipo_animal} Fecha de Nacimiento: {self.fecha_nacimiento}")
class AnimalesEnjaulados(Animal):
    pass

class AnimalesSueltos(Animal):
    pass

class AnimalesAcuaticos(Animal):
    pass


