"""
###**Ejercicio Listas y clases 1.2**
El programa debe:

Contar con:
 *  Contar con una Clase **Persona** con los atributos (dni (int - único), nombre (string), apellido (string))
 *  Contar con una Clase Hija **Empleado** que use el constructor de la clase padre con los atributos:
  -  **funcion** (string)
  -  **año_ingreso** (string 'yyyy')
 *  Se deben crear los siguientes métodos para la clase padre Persona (que heredará la clase hija):
  *  Set y Get dni.

Se deben crear los siguientes métodos para la clase hija.
    
    *  Set y Get funcion.

Se debe contar y crear funciones para un menu que tenga las siguiente opciones,
 - Crear un empleado y guardarlo en una lista_empleados
 - Recorrer la lista de empleados segun DNI, mayor a menor o menor a mayor
 - Recorrer la lista de empleados segun fecha_ingreso, mayor a menor o menor a mayor
 - Eliminar el ultimo empleado agregado

**IMPORTANTE**:

*   Se deben crear metodos y clases a criterio
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""
#from clases import Persona,Empleado

import clases as cl
import gestorEmpleados as ge
from datetime import date, time, datetime

gestor = ge.gestorPersonas()

print(date.today())
while True:
    opcion = input(
    """
-----------MENU PRINCIPAL-----------
Por favor ingrese una opcion:
    1. Crear Empleado
    2. Informacion empleados
    3. Informacion de empleados por año de ingreso de MENOR A MAYOR
    8. Salir
Numero: """
    )
    if (opcion=="1"):
        gestor.crear_empleado()
    elif (opcion=="2"):
        gestor.imprimir_info_empleados()
    elif (opcion=="3"):
        gestor.ordenar_por_fecha_me_a_mayor()
    elif (opcion=="4"):
        pass
    elif (opcion=="5"):
        pass
    elif(opcion=="6"):
        pass
    elif(opcion=="7"):
        pass
    elif (opcion =="8"):
        break