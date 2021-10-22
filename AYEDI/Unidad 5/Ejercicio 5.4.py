"""
##**Ejercicio 5.4**
Crear una funcion que debe:

*   Pedir al usuario una cantidad de tramos de un viaje
*   Pedir al usuario la duracion en minutos de cada tramo (usar listas)
*   Calcular el tiempo total de viaje (motrar en horas)
*   No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

def tramos_viajes():
    while True:
        try:
            while True:
                cant_tramos = int(input("Ingrese la cantidad de tramos del viaje "))
                if cant_tramos <= 0: #detectar si ingreso numeros negativos
                    print("Por favor ingrese un numero positivo.")
                else: 
                    break
        except:
            print("ERROR.")

            lista_minutos = []
            for i in range(cant_tramos):
                while True:
                    try:
                        minutos = int(input(f"Ingrese la duracion del tramo en minutos de {i+1} tramos.  "))
                        if minutos <= 0: #detectar si ingreso numeros negativos
                            print("Por favor ingrese un numero positivo.")
                        else:
                            lista_minutos.append(minutos)
                            break
                    except:
                        print("ERROR.")
            print(f"El tiempo total de viaje en {cant_tramos} tramos es de {sum(lista_minutos)} horas")
            break
        
        #falta lo ultimo

def minutos_a_horas(minutos):
    minutos_iniciales = minutos
    horas_finales = 0
    while minutos > 60:
        minutos = minutos - 60
        horas_finales += 1
    
    print(f"Los {minutos_iniciales} son")
    return horas_finales, minutos

tramos_viajes()