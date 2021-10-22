
"""
   *   Cuyo constructutor debe inicializar los atributos nombre, apellido, edad, ciudad_de_recidencia
*   Se deben crear dos metodos en la clase:
    1.  Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en 
        {ciudad de residencia}
    2.  Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolescente (14 a 22),
         Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)
"""
class Persona:
    nacionalidad = "Argentina"
    #CONSTRUCTOR
    def __init__(self,dni,nombre,apellido,edad,residencia,):
            # Atributos de instancia
            self.dni = dni
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.residencia = residencia
            

    def presentarse(self):
        print(f""" Soy {self.nombre} {self.apellido}, tengo {self.edad} años
vivo en {self.residencia} y mi nacionalidad es {self.nacionalidad}""")

    def rango_edad(self):
        nombre_apellido = (f"{self.nombre}{self.apellido}")
        if (self.edad >0 and self.edad <14):
            print(f"{nombre_apellido} es un niño")
        elif (self.edad >=14 and self.edad <= 22):
            print(f"{nombre_apellido} es adolescente")
        elif (self.edad >22 and self.edad < 30):
            print(f"{nombre_apellido} es joven")
        elif (self.edad >=30 and self.edad <= 50):
            print(f"{nombre_apellido} es adulto")
        else:
            print(f"{nombre_apellido} es mayor")
   