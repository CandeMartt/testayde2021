"""Crear una clase de Figura_Geometrica:
*   Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño 
    (por defecto "pequeño")"""

class FiguraGeometrica:
    #CONSTRUCTOR
    def __init__(self,tipo_de_figura, color, tamaño ="pequeño"):
            # Atributos de instancia
            self.tipo_de_figura = tipo_de_figura
            self.color = color
            self.tamaño = tamaño


    def presentar(self):
        print(f"""La figura {self.tipo_de_figura} es de color {self.color} y es de tamaño {self.tamaño} """)

    def cambiar_color(self, color_nuevo):
        print(f"Cambie del color {self.color} al color {color_nuevo}")
        self.color = color_nuevo
        
    def cambiar_color(self): #esta bien, pero es recomendable dejar los metodos sin ingresar nada
        tipo_de_figura = input("Indique la figura a la cual desea cambiarle el color: ")
        if self.tipo_de_figura == tipo_de_figura:
            nuevo_color = input("Ingrese el nuevo color: ")
            self.color = nuevo_color
            print(f"El color de la figura {self.tipo_de_figura} es {self.color}")
        else:
            print(f"La figura {tipo_de_figura} no se encuentra en esta base de datos.")

    def verificar(self):
        if self.tamaño == "pequeño":
           self.tamaño = "grande"
        print(f"El tamaño de la figura es {self.tamaño}")
    


figura_1 = FiguraGeometrica("triangulo","blanco")
figura_1.presentar()
#figura_1.cambiar_color()
figura_1.verificar()

