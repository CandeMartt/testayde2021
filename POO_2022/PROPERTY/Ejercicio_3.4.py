"""
###**Ejercicio 3.4**
Crear una clase Persona con atributos DNI, nombre, apellido encapsulados, 
de tal forma de poder acceder y modificar los atributos unicamente 
con metodos get y set utilizando el decorador property

Probar todos los requerimientos
"""

class Persona:
    def __init__(self,dni,nombre,apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido

    @property 
    def dni(self): #get
        return self.__dni

    @dni.setter
    def dni(self,nuevo_dni): #set
        self.__dni = nuevo_dni
    
    @dni.deleter
    def dni(self): #delete
        del self.__dni 

    @property
    def nombre(self): #get
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevo_nombre): #set
        self.__nombre = nuevo_nombre
    
    @nombre.deleter
    def nombre(self): #delete
        del self.__nombre

    @property
    def apellido(self): #get
        return self.__apellido

    @apellido.setter
    def apellido(self,nuevo_apellido): #set
        self.__apellido = nuevo_apellido
    
    @apellido.deleter
    def apellido(self): #delete
        del self.__apellido

persona_1 = Persona(1234, "Juan", "Perez")
print(persona_1.dni)
persona_1.dni = 5678
print(persona_1.dni)
#del persona_1.dni aca debe saltar error porque ya no existiria el atributo
#print(persona_1.dni)


        