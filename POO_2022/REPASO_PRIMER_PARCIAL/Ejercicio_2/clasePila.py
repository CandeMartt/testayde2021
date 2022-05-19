#clase PILA
class Pila:
    def __init__(self):
      #print("Crea una pila vacía.")
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

    def eliminar_impar(self,pila):
      pila_aux = Pila()
      for i in range(pila.get_tamanio()):
          dato=pila.desapilar()
          if type(dato) == type(2) and dato%2 == 0: 
            pila_aux.apilar(dato)
          elif type(dato) == type('str'):
            pila_aux.apilar(dato)
      for i in range(pila_aux.get_tamanio()):
          pila.apilar(pila_aux.desapilar())
      print(pila)
                  
  