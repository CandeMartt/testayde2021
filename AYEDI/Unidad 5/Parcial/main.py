#29/09/2021
'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: 1° Examen
 APELLIDO Y NOMBRE: Martinez, María Candela
 DNI: 42787335
 CARRERA: Analista de Sistemas
 AÑO: 2021 
 Se envia mail con asunto: "[AYEDI 2021 - Apellido, Nombre - 1°Examen]"
 ************************************************************
 Items a evaluar:
 1. Requerimientos y comprension de consignas
 2. Estructura (modularización), legibilidad y comentarios del codigo.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Gestión de alumnos y Materias"

Introduccion: 
    El siguiente programa consiste en un software de gestion de alumnos y gestion de materias
    de una institucion educativa.
    El programa debe permitir agregar y quitar alumnos al sistema junto con su informacion personal: 
    Nombre, Edad y mail.
    El programa debe permitir agregar Materias al sistema.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail)
    2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)
       Verificando: Que el nombre_usuario no exista previamente, la edad entre 10 y 18 años y que el mail cuente con un @.
       (Ayuda: metodo in de list sirve tambien para strings)
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias)
    5. Agregar materias al sistema (verificando que no exista previamente)
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

Alumnos = [["Jose_Fernandez","Juan_Lopez"],[17,15],["josefernadez@gmail.com", "juanlopez@gmail.com"]]
Materias = ["Quimica","Biologia"]

import funciones as fn

while True:
                opcion = input(
                """Por favor, elija una opcion:
                1. Ver lista de alumnos
                2. Agregar Alumno
                3. Editar edad de Alumno
                4. Ver lista de materias
                5. Agregar materias  
                6- Salir
                Numero """)

                if opcion == "1":
                    fn.lista_alumnos(Alumnos)
                elif opcion == "2":
                    Alumnos = fn.agregar_alumno(Alumnos)
                elif opcion == "3":
                    Alumnos = fn.editar_edad(Alumnos)
                elif opcion == "4":
                    fn.lista_materias(Materias)
                elif opcion == "5":
                    Materias = fn.agregar_materias(Materias)
                elif opcion =="6":   
                    break
                else:
                    print("No ingreso una opcion correcta")