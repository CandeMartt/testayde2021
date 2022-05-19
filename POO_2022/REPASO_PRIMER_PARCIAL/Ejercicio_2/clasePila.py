#clase PILA
class Pila:
    def __init__(self):
      print("Crea una pila vacía.")
      self.items=[]
    
    def apilar(self, x):
      #print(f"Agrega el elemento {x} a la pila.")
      self.items.append(x)
    
    def desapilar(self):
      try:
        return self.items.pop()
      except IndexError:
        raise ValueError("La pila está vacía")
    
    def ver_pila(self):
      print("-----PILA-----")
      for i in reversed(self.items):
        print(i)
      print("--------------")
    
    def get_tamanio(self):
      return len(self.items)

    def eliminar_impar(self):
      pila_aux = []
      while len(self.items)!= 0:
          dato=self.items.pop()
          if dato %2 == 0:
              pila_aux.append(dato)
      while len(pila_aux)!= 0:
          self.items.append(pila_aux.pop())
      print(self.items)
                  
  