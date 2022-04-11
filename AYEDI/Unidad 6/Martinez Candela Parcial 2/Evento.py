"""
Requerimientos:
El programa debe:
*   Contar con una Clase Evento con los atributos (nombre_evento (único), fecha, hora, lugar)
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más:
        - EventoPersonal (Atributo: organizador (nombre de la persona que organiza))
        - EventoLaboral (Atributo: obligatorio "True o False" (por defecto = True))
        
*   Se deben crear 4 métodos para la clase padre Evento (que heredaran las clases hijas):
        1. Mostrar información: Que indique el nombre_evento, fecha y lugar del evento 
        2. Obtener tipo de evento (tipo de clases heredadas o padre)
        3. Setear Fecha y Hora (Setearán la Fecha y Hora en una misma función)
        4. Setear lugar (Setear el lugar)
"""
#Clase padre EVENTO
class Evento:
    #CONSTRUCTOR
    def __init__(self, nombre_evento, fecha, hora, lugar):
        self.nombre_evento = nombre_evento
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar

    def get_nombre_evento(self):
        return self.nombre_evento

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_lugar(self):
        return self.lugar

#Los cuatro métodos pedidos
    def presentarse(self):
        print("")
        print(f" Nombre del evento: {self.nombre_evento} / Fecha: {self.fecha} / Lugar del evento: {self.lugar}")
        print("")

    def tipo_objeto(self):
        print("Evento tipo: ", type(self).__name__)
    
    def set_estado(self, nueva_fecha, nueva_hora):
        self.fecha = nueva_fecha
        self.hora = nueva_hora
        
    def set_lugar(self, nuevo_lugar):
        self.lugar = nuevo_lugar

#Clase hija de Evento  
class EventoPersonal(Evento):
        def __init__(self, nombre_evento, fecha, hora, lugar, organizador):
                super().__init__(nombre_evento, fecha, hora, lugar)
                self.organizador = organizador

#Clase hija de Evento
class EventoLaboral(Evento):
        def __init__(self, nombre_evento, fecha, hora, lugar, obligatorio = True):
                super().__init__(nombre_evento, fecha, hora, lugar)
                self.obligatorio = obligatorio