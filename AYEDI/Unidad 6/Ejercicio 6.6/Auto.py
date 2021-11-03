"""
####**Ejercicio 6.6 (Empresa de Taxis)**
*   Simular una empresa de taxis que cuente con dos clases: Autos y Chofer
*   La Clase auto tiene los atributos (patente, modelo, año, marca, nombre_Chofer (objeto clase Choferes))
*   La Clase Chofer tiene los atributos (nombre, apellido, dni, fecha nacimiento, Residencia)
*   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorTaxis)**:
    1. Crear instancias de choferes y guardarlos en una
    2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    3. Modificar el chofer de un auto
    4. Modificar el lugar de residencia del chofer indicando su nombre
    5. imprmiir lista de choferes (con toda su informacion)
    6. imprimir lista de autos (con toda su informacions)
*   Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""

class Auto:
    #CONSTRUCTOR
    def __init__(self, patente,modelo, año, marca, nombre_chofer):
        self.patente = patente
        self.modelo = modelo
        self.año = año
        self.marca = marca
        self.nombre_chofer = nombre_chofer

    def get_patente(self):
        return self.patente

    def get_chofer(self):
        return self.nombre_chofer

    def set_chofer(self,nuevo_nombre):
        self.nombre_chofer =  nuevo_nombre

    def imprimir_informacion(self):
        print(f"Patente:{self.patente} - Año{self.año} - marca/modelo {self.marca}/{self.modelo} - Chofer {self.nombre_chofer}") 
       
        