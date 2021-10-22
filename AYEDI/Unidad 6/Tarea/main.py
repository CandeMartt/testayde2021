import Autos as au
import funciones as fn
while True:
    condicion=input(
    """
Por favor ingrese la opcion que desee utilizar
    1. Crear un auto
    2. Mostrar todos los autos en tabla
    3. Presentar auto por auto
Numero: """)

    if condicion == "1": 
       fn.crar_auto()
    elif condicion =="2": 
       fn.tabla_lista()
    elif condicion =="3": 
       fn.listar_autos()
    elif condicion =="4": 
        print("Gracias por utilizar este programa! Hasta luego!")
        break