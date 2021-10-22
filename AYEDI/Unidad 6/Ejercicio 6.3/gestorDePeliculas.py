import Peliculas as pl
lista_peliculas = []
lista_genero = ["Comedia", "Drama", "Ciencia ficcion"]
"""El programa debe: gestorDePeliculas
*   Tener un menu con 7 opciones:
    1. Crear una pelicula y guardar su nombre (instancia) en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
    6. Verificar el año de la pelicula
    7  Modificar puntuacion de la pelicula (entre 1 y 10)
    """
class GestorDePeliculas:
    def verificar_pelicula(self,nombre_pelicula ="null"):
        while True: 
            if nombre_pelicula == "null":
               nombre_pelicula = input("Por favor ingrese el nombre de la pelicula: ").capitalize()
            
            for pelicula in lista_peliculas:
                if nombre_pelicula  == pelicula.nombre:
                    print("Esta pelicula ya existe")
                    return True

            print("Esta pelicula no existe")
            return False
                
    def crar_peliculas(self):
        #nombre pelicula
        while True: 
            nombre = input("Por favor ingrese el nombre de la pelicula: ").capitalize()
            if (not self.verificar_pelicula(nombre)):
                break

        #año pelicula
        while True:
            try:
                año = int(input("Por favor ingrese el año de la pelicula: "))
                if año <=0:
                    print("El año de la película debe ser mayor de cero")
                elif (año >= 1960) and (año <= 2021):
                    break
                else:
                    print("El año debe ser mayor o igual a 1960 y menor o igual a 2021")
            except:
                print("ERROR.")

        #genero
        while True:
            genero = input("Ingrese el genero de la pelicula: ").capitalize()
            if genero not in lista_genero:
                print("Este genero no esta en nuestra base de datos. Por favor ingrese otro.")
            else:
                break

        #nacionalidad
        nacionalidad = input("Ingrese de que nacionalidad es la pelicula: ")

        #puntuacion
        try:
            puntuacion = int(input("Ingrese la puntuacion de la pelicula: "))
        except:
            print("ERROR.") 

        nombre_instancia = nombre
        nombre_instancia = pl.Peliculas(nombre, año, genero, nacionalidad, puntuacion)
        lista_peliculas.append(nombre_instancia)

    def imprimir_lista():
        for peliculas in lista_peliculas:
            print(peliculas.nombre)

    def año_determinado():
        año_determ = input("Ingrese un año determinado: ")
        for año in lista_peliculas:
            acum = 0
            if año_determ == año:
                acum += 1
                print(f"Las peliculas ")

    def pelicula_especifica(): 
        nombre = input("Ingrese el nombre de la pelicula que desea buscar: ")
        for pelicula in lista_peliculas:
            nombre == pelicula.presentar()
