class Casa:
    def __init__(self, puerta, ventana, calefactor):
        self.puerta = puerta()
        self.ventana = ventana()
        self.calefactor = calefactor()

class Puerta:
    def abrir(self):
        print("Puerta -> Abierta")
    def cerrar (self):
        print("Puerta -> Cerrada")

class Ventana:
    def __init__(self, persiana):
        self.persiana = persiana
    def abrir(self):
        print("Ventana -> Abierta")
    def cerrar (self):
        print("Ventana -> Cerrada")

class Persiana:
    def subir(self):
        print("Persiana-> Subida")
    def bajar (self):
        print("Persiana -> Bajada")

class Calefactor:
    def __init__(self, temperatura):
        self.temperatura = temperatura
    def encender(self):
        print("Calefactor -> Encendido")
    def apagar (self):
        print("Calefactor -> Apagado")
    def fijar_temperatura (self,nueva_temperatura):
        self.temperatura = nueva_temperatura

persiana_1 = Persiana()
ventana_1 = Ventana(persiana_1)
puerta_1 = Puerta()
calefactor_1 = Calefactor(28)
casa = Casa(puerta_1,ventana_1,calefactor_1)
print(casa.puerta.abrir())