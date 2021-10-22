"""
###**Ejercicio 6.1**
Crear una clase de Persona:
*   Cuyo constructutor debe inicializar los atributos nombre, apellido, edad, ciudad_de_recidencia
*   Se deben crear dos metodos en la clase:
    1.  Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en 
        {ciudad de residencia}
    2.  Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolescente (14 a 22),
         Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)
*
    Menu:
    1. Para crear personas
    2. Segun el nombre de persona indicar edad"""
import Persona as pn
import funciones as fn
while True:
    condicion=input(
    """
Por favor ingrese la opcion que desee utilizar
    1. Crear persona
    2. Mostrar rango etario
    3. Listar Personas
Numero: """)

    if condicion == "1": 
       fn.crar_personas()
    elif condicion =="2": 
       fn.consultar_rango()
    elif condicion =="3": 
       fn.listar_personas()
    elif condicion =="4": 
        print("Gracias por utilizar este programa! Hasta luego!")
        break