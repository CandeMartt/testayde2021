"""
El programa debe:

Contar con:

Contar con una Clase Persona con los atributos (dni (int - único), nombre (string), apellido (string))
Contar con una Clase Hija Empleado que use el constructor de la clase padre con los atributos:
funcion (string)
año_ingreso (string 'yyyy')
Se deben crear los siguientes métodos para la clase padre Persona (que heredará la clase hija):
Set y Get dni.
Se deben crear los siguientes métodos para la clase hija.

*  Set y Get funcion.
Se debe contar y crear funciones para un menu que tenga las siguiente opciones,

Crear un empleado y guardarlo en una lista_empleados
Recorrer la lista de empleados segun DNI, mayor a menor o menor a mayor
Recorrer la lista de empleados segun fecha_ingreso, mayor a menor o menor a mayor
Eliminar el ultimo empleado agregado
IMPORTANTE:

Se deben crear metodos y clases a criterio
Gestionar posibles errores
Estructurar el programa a criterio propio

"""
import gestorPersona as gp
gestor = gp.gestorPersonas()

while True:
    opcion = input(
    """
-----------MENU PRINCIPAL-----------
Por favor ingrese una opcion:
    1. Crear Empleado
    2. Informacion empleados
    3. Informacion de empleados por dni de MENOR A MAYOR
    4. Informacion de empleados por dni de MAYOR A MENOR
    5. Informacion de empleados por año de ingreso de MENOR A MAYOR
    6. Informacion de empleados por año de ingreso de MAYOR A MENOR
    7. Eliminar el ultimo empleado de la lista
    8. Salir
Numero: """
    )
    if (opcion=="1"):
        gestor.crear_empleado()
    elif (opcion=="2"):
        gestor.imprimir_info_empleados()
    elif (opcion=="3"):
        gestor.imprimir_por_dni()
    elif (opcion=="4"):
        gestor.imprimir_por_dni_mayor_a_menor()
    elif (opcion=="5"):
        gestor.imprimir_por_fecha_de_ingreso()
    elif(opcion=="6"):
        gestor.imprimir_por_fecha_de_ingreso_2()
    elif(opcion=="7"):
        gestor.eliminar_ultimo_empleado()
    elif (opcion =="8"):
        break