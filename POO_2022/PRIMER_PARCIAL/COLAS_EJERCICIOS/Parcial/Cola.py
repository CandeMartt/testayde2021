class Cola:
    def __init__(self):
        self.items=[]

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
        return self.items == []
    
    def ver_cola(self): 
        for i in range(len(self.items)-1, -1, -1):
            if i == len(self.items)-1:
                print("Final", end =" ")
            print(self.items[i], end =" ")
            if i == 0:
                print("Frente", end =" ")
    
    #AQUI CREAR EL METODO DEL EJERICIO 2
    def mover_al_frente(self,valor):
      for i in self.items:
        try:
          self.items.append(self.items.remove(valor)(0))
        except:
          print("COLA VACIA")