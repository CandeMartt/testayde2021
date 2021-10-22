class Autos:
    #CONSTRUCTOR
    def __init__(self,codigo,nombre_auto,color,marca,puertas):
            # Atributos de instancia
            self.codigo = codigo
            self.nombre_auto = nombre_auto
            self.color = color
            self.marca = marca
            self.puertas = puertas

            

    def presentar_auto(self):
        print(f"""El {self.nombre_auto} es de color {self.color}, es de la marca {self.marca}
y tiene {self.puertas} puertas""")

