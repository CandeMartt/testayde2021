"""
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad
 
Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una
1.   Particular
2.   PickUp
3.   Deportivo
"""

class Vehiculos:
#CONSTRUCTOR
    def __init__(self, patente,marca, año, origen):
        self.patente = patente
        self.marca = marca
        self.año = año
        self.origen = origen

    def presentarse(self):
        print(f"Vehiculo con patente {self.patente} de la marca {self.marca}, del año {self.año} y de origen {self.origen}")

    def tipo_vehiculo(self):
        print ("Soy un vehiculo tipo", type(self).__name__)

    def acelerar(self):
        pass

    def retroceder(self):
        pass

    def obtener_velocidad_max(self):
        pass

    def setear_velocidad_max(self):
        pass

class VehiculoParticular(Vehiculos):
    def __init__(self,patente,marca, año, origen,velocidad_max = 130):
        super().__init__(patente,marca, año, origen)
        self.velocidad_max = velocidad_max

    def acelerar(self):
        print("Estoy acelerando. Soy un Vehiculo Particular!")

    def retroceder(self):
        print("Estoy retrocediendo. Soy un Vehiculo Particular!")

    def obtener_velocidad_max(self):
        print(f"La velocidad máxima del vehiculo persona es {self.velocidad_max} ")

    def setear_velocidad_max(self, velocidad_nueva):
        print (f"La velocidad máxima del vehiculo particular era {self.velocidad_max} y ahora es {velocidad_nueva}")
        self.velocidad_max = velocidad_nueva


class VehiculoPickUp(Vehiculos):
    def __init__(self,patente,marca, año, origen,velocidad_max = 180):
        super().__init__(patente,marca, año, origen)
        self.velocidad_max = velocidad_max

    def acelerar(self):
        print("Estoy acelerando. Soy un Vehiculo PickUp!")

    def retroceder(self):
        print("Estoy retrocediendo. Soy un Vehiculo PickUp!")

    def obtener_velocidad_max(self):
        print(f"La velocidad máxima del vehiculo PickUp es {self.velocidad_max} ")

    def setear_velocidad_max(self,velocidad_nueva):
        print (f"La velocidad máxima del vehiculo PickUp era {self.velocidad_max} y ahora es {velocidad_nueva}")
        self.velocidad_max = velocidad_nueva


class VehiculoDeportivo(Vehiculos):
    def __init__(self,patente,marca, año, origen,velocidad_max = 200):
        super().__init__(patente,marca, año, origen)
        self.velocidad_max = velocidad_max

    def acelerar(self):
        print("Estoy acelerando! Soy un Vehiculo Deportivo!")

    def retroceder(self):
        print("Estoy retrocediendo! Soy un Vehiculo Deportivo!")

    def obtener_velocidad_max(self):
        print(f"La velocidad máxima del vehiculo deportivo es {self.velocidad_max} ")

    def setear_velocidad_max(self,velocidad_nueva):
        print (f"La velocidad máxima del vehiculo deportivo era {self.velocidad_max} y ahora es {velocidad_nueva}")
        self.velocidad_max = velocidad_nueva
