#30/09/2021
"""
El programa debe:
Simular una base de datos de peliculas y series con la capacidad de agregar, buscar, eliminar y filtrar peliculas y series.
Debe comenzar con las siguientes peliculas y series en un diccionario:
base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }
Contar con 5 funciones disponibles en el menu:
1. Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
2. Agregar nuevas peliculas o series (que no esten) en la base.
3. Eliminar peliculas o series de la base.
4. Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere ver de la 2° a la 4° una lista ).
5. Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), se liste las peliculas que contengan la palabra "el").
"""

base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["Prision break", "La casa de papel" , "Los simpsons"]
        }

import funciones as fn


while True:
    condicion=input(
    """
Por favor ingrese la opcion que desee utilizar
    1. Mostrar todas las series o peliculas que hay en el catálogo
    2. Agregar series o peliculas al catálogo
    3. Eliminar series o peliculas al catálogo
    4. Mostrar series o peliculas según en las posiciones que este en el catálogo
    5. Buscar series o peliculas ingresando una palabra clave
    6. Salir
Numero: """)
        
    if condicion == "1": 
        fn.mostrar_bases(base)
    elif condicion =="2": 
        base = fn.agregar_peliculas_series(base)
    elif condicion =="3": 
        base = fn.eliminar_peliculas_series(base)
    elif condicion =="4":   
        fn.mostras_lugares_series_peliculas(base)
    elif condicion =="5": 
        fn.buscar_palabras_requeridas(base)
    elif condicion == "6":
        print("Gracias por utilizar este programa! Hasta luego!")
        break
    else:
        print("No ingreso una opcion correcta")

