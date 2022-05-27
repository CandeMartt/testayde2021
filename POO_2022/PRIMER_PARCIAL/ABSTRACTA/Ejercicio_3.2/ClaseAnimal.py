"""
Ejercicio 3.2
Crear una clase abstracta Animal con 4 metodos. (Hablar, Mover, Dormir, Comer) y 
dos clases Gato y Perro que hereden la clase Animal.
Luego crear un menu para crear animales y guardarlos en una lista.
"""
from abc import ABC
from abc import abstractmethod
class Animal_abs(ABC):
  @abstractmethod
  def hablar_animal(self):
      pass

  @abstractmethod
  def mover_animal(self):
      pass

  @abstractmethod
  def dormir_animal(self):
      pass

  @abstractmethod
  def comer_animal(self):
      pass


class Animal:
    #contructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad


    def hablar_animal(self):
        print("Animal -> Hablar")
    def mover_animal(self):
        print("Animal -> Mover")
    def dormir_animal(self):
        print("Animal -> Dormir")
    def comer_animal(self):
        print("Animal -> Comer")

    #generico  
    def tipo_animal(self):
            print("Soy un Animal del tipo", type(self).__name__)
    def get_especie(self):
        return self.especie
    def set_especie(self, nueva_especie):
        self.especie = nueva_especie
    def get_edad(self):
        return self.edad
    def set_edad(self, nueva_edad):
        self.edad= nueva_edad

class Perro(Animal):
    def __init__(self, especie, edad, raza):
        super().__init__(especie, edad)
        self.raza = raza

    def get_raza(self):
        return self.raza

    def set_raza(self, nueva_raza):
        self.raza= nueva_raza

class Gato(Animal):
    def __init__(self, especie, edad, raza):
        super().__init__(especie, edad)
        self.raza = raza

    def get_raza(self):
        return self.raza

    def set_raza(self, nueva_raza):
        self.raza= nueva_raza

Nuevo_Animal= Gato("gato",12,"Calle")
Nuevo_Animal.comer_animal()
print(Nuevo_Animal.tipo_animal())