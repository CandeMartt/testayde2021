def mostrar_bases(base):
    while True:
        base_mostrar = input("""
-------------CATÁLOGO-------------
Ingrese si requiere ver:
    1. la lista de peliculas
    2. la lista de series
    3. Salir
Opcion:   """
        )
        if base_mostrar =="1":
            print(f"---------Peliculas---------")
            for i in range(len(base.get("peliculas"))):
                print(base.get("peliculas")[i])
        elif base_mostrar =="2":
            print(f"---------Series---------")
            for i in range(len(base.get("series"))):
                print(base.get("series")[i])
        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")

def agregar_peliculas_series(base):
    while True:
        base_mostrar = input("""
-------------AGREGAR AL CATÁLOGO-------------
Ingrese si requiere:
    1. Agregar peliculas
    2. Agregar series 
    3. Salir
Opcion:   """
            )
        if base_mostrar =="1":
            while True:
                nombre_pelicula = input("Ingrese el nombre de la nueva pelicula: ").casefold().capitalize()
                if nombre_pelicula not in base.get("peliculas"):
                    base.get("peliculas").append(nombre_pelicula)
                    break
                else:
                    print("Esa pelicula ya se encuentra en la base de datos")

        elif base_mostrar =="2":
            while True:
                nombre_serie = input("Ingrese el nombre de la nueva serie: ").casefold().capitalize()
                if nombre_serie not in base.get("series"):
                    base.get("series").append(nombre_serie)
                    break
                else:
                    print("Esa serie ya se encuentra en la base de datos")
        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")
    return base

def eliminar_peliculas_series(base):
    while True:
        base_mostrar = input("""
-------------ELIMINAR DEL CATÁLOGO-------------
Ingrese si requiere:
    1. Eliminar peliculas
    2. Eliminar series 
    3. Salir
Opcion:   """
            )
        if base_mostrar =="1":
            lista_pelicula = base.get("peliculas")
            print(lista_pelicula)
            while True:
                nombre_pelicula = input("Ingrese el nombre de la pelicula a eliminar: ").casefold().capitalize()
                if nombre_pelicula in lista_pelicula:
                    base.get("peliculas").remove(nombre_pelicula)
                    break
                else:
                    print("Esa pelicula no se encuentra en la base de datos")

        elif base_mostrar =="2":
            lista_series = base.get("series")
            print(lista_pelicula)
            while True:
                nombre_serie = input("Ingrese el nombre de la serie a eliminar: ").casefold().capitalize()
                if nombre_serie in lista_series:
                    base.get("series").remove(nombre_serie)
                    break
                else:
                    print("Esa serie ya se encuentra en la base de datos")
        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")
    return base

def mostras_lugares_series_peliculas(base):
    while True:
        base_mostrar = input("""
-------------POSICIONES EN EL CATÁLOGO-------------
Ingrese si requiere:
    1. Ver peliculas
    2. Ver series 
    3. Salir
Opcion:   """
            )
        if base_mostrar =="1":
            list_peliculas = base.get("peliculas") 
            primera_posicion =int(input("Ingrese la primera posición: "))
            segunda_posicion = int(input("Ingrese la ultima posición: "))
            for i in range(primera_posicion-1,segunda_posicion):
                print(list_peliculas[i],end = "-")
        elif base_mostrar =="2":
           list_series= base.get("series")
           inicio= int(input("Ingrese desde donde desea ver: "))
           fin = int(input("Ingrese hasta donde desea ver: "))
           for i in (list_series[inicio-1:fin]):
            print(i,end = "-")
 

def buscar_palabras_requeridas(base):
    while True:
        base_mostrar = input("""
-------------BUSCAR PALABRAS CLAVES EN EL CATÁLOGO-------------
Ingrese si requiere:
    1. Ver peliculas
    2. Ver series 
    3. Salir
Opcion:   """
            )
        if base_mostrar == "1":
            lista_peliculas = base.get("peliculas")
            palabra_requerida = input("Ingrese la palabra a buscar: ")
            for pelicula in lista_peliculas:
                if palabra_requerida in pelicula:
                    print(f"La palabra {palabra_requerida} esta en {pelicula}")
                else:
                    print("No se encontró ninguna película con esa palabra clave")
        elif base_mostrar == "2":
            lista_series = base.get("series")
            palabra_requerida = input("Ingrese la palabra a buscar: ")
            for i in lista_series:
                if palabra_requerida in i:
                    print(f"La palabra {palabra_requerida} esta en {i}")
                else:
                    print("No se encontró ninguna serie con esa palabra clave")
        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")

