"""
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""

import Vehiculos as vh
lista_autos = []

class GestorDeVehiculos:
    def __init__(self):
        pass

    def crear_vehiculo(self):
        while True:
            condicion=input(
            """
        ---------------- CREAR VEHÍCULO ----------------
        Por favor ingrese la opcion que desee utilizar
            1. Vehículo Genérico
            2. Vehículo Particular
            3. Vehículo Deportivo
            4. Vehículo PickUp
        Numero: """)

            if condicion == "1" or condicion == "2" or condicion == "3" or condicion ==  "4":
                break
            else:
                print("Opcion incorrecta")
        while True:
            patente = input("Ingrese la patente del vehículo: ")
            if patente in lista_autos:
                print("La patente ya se encuentra en el sistema")
            else:
                break
        marca = input("Ingrese la marca del vehículo: ")  
        while True:
            try:
                año = int(input("Ingrese el año del vehículo: "))
                break
            except:
                print("ERROR.")

        origen = input("Ingrese el origen del vehículo: ")

        if condicion == "2" or condicion == "3" or condicion ==  "4":
            while True:
                try:
                    velocidad_max = int(input("Ingrese la velocidad máxima del vehículo: "))
                    break
                except:
                    print("ERROR.")

        if condicion == "1":
            nombre_instancia = vh.Vehiculos(patente, marca, año, origen)
        elif condicion == "2":
            nombre_instancia = vh.VehiculoParticular(patente, marca, año, origen, velocidad_max)
        elif condicion == "3":
            nombre_instancia = vh.VehiculoDeportivo(patente, marca, año, origen)
        
        if condicion == "4":
            nombre_instancia = vh.VehiculoPickUp(patente, marca, año, origen)

        lista_autos.append(nombre_instancia)

    def listar_vehiculos(self):   
        for vehiculo in lista_autos:
                vehiculo.presentarse()
                vehiculo.tipo_vehiculo()
    
    def cambiar_velocidad(self):
        for vehiculo in lista_autos:
            print(vehiculo.patente)

        #falta un while
        patente = input("Ingrese la patente dl vehiculo a cambiar la velocidad: ")

        for vehiculo in lista_autos:
            if vehiculo.patente == patente:
                if(type(vehiculo).__name__ != "Vehiculos"):
                    while True:
                        try:
                            velocidad_max= int(input("Ingrese la velocidad máxima: "))
                            break
                        except:
                            print("ERROR.")
                    vehiculo.setear_velocidad_max(velocidad_max)
                else: 
                    print("El vehiculo generico no tiene velocidad máxima.")



    def calcular_tiempo(self):
        for vehiculo in lista_autos:
            print(vehiculo.patente)


        patente = input("Ingrese la patente del vehiculo a cambiar la velocidad: ")
        for vehiculo in lista_autos:
            if vehiculo.patente == patente:
                if(type(vehiculo).__name__ != "Vehiculos"):
                    while True:
                        try:
                            km= int(input("Ingrese el km: "))
                            print(f"El tiempo en recorrer esos {km} serán: {km/vehiculo.velocidad_max} ")
                            break
            
                        except:
                            print("ERROR.")
                else: 
                    print("El vehiculo generico no tiene velocidad máxima.")



