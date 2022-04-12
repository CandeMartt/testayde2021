class Rectangulo:
     #  El `self` se pasa como parámetro de entrada del método. Es una variable que representa la instancia de la clase, y **deberá estar siempre ahí.**
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class RectanguloPequeno(Rectangulo):
    def __init__(self,base,altura,color):
        super().__init__(base,altura)
        self.color = color



rectangulo_1 = Rectangulo(2,3)
print(f"Altura del rectangulo: {rectangulo_1.calcular_area()}")
