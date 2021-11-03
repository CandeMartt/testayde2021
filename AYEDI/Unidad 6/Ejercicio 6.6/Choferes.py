"""
####**Ejercicio 6.6 (Empresa de Taxis)**
*   La Clase Chofer tiene los atributos (nombre, apellido, dni, fecha nacimiento, Residencia)
*   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorTaxis)**:

    4. Modificar el lugar de residencia del chofer indicando su nombre
    5. imprmiir lista de choferes (con toda su informacion)
"""

class Choferes:
    #CONSTRUCTOR
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, residencia):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.residencia = residencia
    
    def get_nombre(self):
        return self.nombre
      
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_dni(self):
        return self.dni
        
    def modificar_residencia(self,nueva_residencia):
        self.residencia = nueva_residencia

    def imprimir_info_choferes(self):
        print(f"Chofer: {self.get_nombre} {self.apellido} - DNI: {self.dni} - Nacimiento: {self.fecha_nacimiento} - Residencia {self.residencia} ")

    

    
