"""
Crear una clase Persona con atributos: nombre, apellido, edad encapsulados.

Crear 2 metodos estaticos
-calcular_tiempo_estudio(paginas,tiempoxpagina)
-calcular_salario(horasxdia,precioxhora)

Crear 2 metodos de instancia
get_nombre_apellido
get_edad
"""
class Persona:
    def __init__(self,nombre,apellido,edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @staticmethod
    def calcular_tiempo_estudio(paginas,tiempoxpagina):
        print (f"El tiempo de estudio sera de: {paginas*tiempoxpagina}")
    @staticmethod
    def calcular_salario(horasxdia,precioxhora):
        print (f"El tiempo de estudio sera de: {horasxdia*precioxhora}")


    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
    @property
    def edad(self):
        return self.__edad

persona_1 = Persona("Juan", "Perez", 33)
persona_1.calcular_tiempo_estudio(200,30)
persona_1.calcular_salario(8,350)
print(persona_1.nombre)
print(persona_1.apellido)
print(persona_1.edad)

