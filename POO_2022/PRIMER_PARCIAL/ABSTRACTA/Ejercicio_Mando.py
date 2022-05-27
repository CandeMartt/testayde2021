from abc import ABC
from abc import abstractmethod
class Mando_abs(ABC):
  @abstractmethod
  def siguiente_canal(self):
      pass

  @abstractmethod
  def canal_anterior(self):
      pass

  @abstractmethod
  def subir_volumen(self):
      pass

  @abstractmethod
  def bajar_volumen(self):
      pass

class MandoSamsung(Mando_abs):
    def __init__(self, color, tamanio):
        self.color = color
        self.tamanio = tamanio
       
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")

    def get_color(self):
        return self.color
    def get_anio(self):
        return self.tamanio

mando_samsung = MandoSamsung("rojo",30)
mando_samsung.subir_volumen()
print(mando_samsung.get_color())