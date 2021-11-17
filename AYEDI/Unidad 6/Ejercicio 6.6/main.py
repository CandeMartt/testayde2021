"""
####**Ejercicio 6.6 (Empresa de Taxis)**
*   Simular una empresa de taxis que cuente con dos clases: Autos y Chofer
*   La Clase auto tiene los atributos (patente, modelo, año, marca, nombre_Chofer (objeto clase Choferes))
*   La Clase Chofer tiene los atributos (nombre, apellido, dni, fecha nacimiento, Residencia)
*   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorTaxis)**:
    1. Crear instancias de choferes y guardarlos en una
    2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    3. Modificar el chofer de un auto
    4. Modificar el lugar de residencia del chofer indicando su nombre
    5. imprmiir lista de choferes (con toda su informacion)
    6. imprimir lista de autos (con toda su informacions)
*   Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""


import gestorTaxis as gt

gestor = gt.gestorTaxis()

while True:
    opcion = input(
    """
---------------- MENU PRINCIPAL ----------------
Por favor ingrese la opcion que desee utilizar
    1. Crear Chofer
    2. Crear Auto
    3. 
    4. 
    5. Imprmiir lista de choferes
    6. Imprimir lista de autos
    7. Salir
Número: """
    )
    if (opcion=="1"):
        gestor.crear_instancia_chofer()
    elif (opcion=="2"):
        gestor.crear_instancia_auto()
    elif (opcion=="3"):
        gestor.modificar_chofer_auto()
    elif (opcion=="4"):
        pass
    elif (opcion=="5"):
        gestor.imprimir_info_choferes()
    elif (opcion=="6"):
        gestor.imprimir_info_autos()
    elif (opcion=="7"):
        break
    else:
        print("ninguna opcion correcta")