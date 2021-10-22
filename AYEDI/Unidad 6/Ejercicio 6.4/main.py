"""
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad
 
Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una
1.   Particular
2.   PickUp
3.   Deportivo
 
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""
import Vehiculos as vh
import gestorDeVehiculos as gv
gestor = gv.GestorDeVehiculos()

while True:
    condicion=input(
    """
---------------- MENU PRINCIPAL ----------------
Por favor ingrese la opcion que desee utilizar
    1. Crear vehiculo
    2. Listar autos (presentación y tipo)
    3. Cambiar velocidades
    4. 
    5. 
    6. Salir
Numero: """)

    if condicion == "1": 
        gestor.crear_vehiculo()
    elif condicion =="2": 
        gestor.listar_vehiculos()
    elif condicion =="3": 
        gestor.cambiar_velocidad()
    elif condicion == "4":
        gestor.calcular_tiempo()
    elif condicion == "5":
        pass
    elif condicion =="6": 
        print("Gracias por utilizar este programa! Hasta luego!")
        break