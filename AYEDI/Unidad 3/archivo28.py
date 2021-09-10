"""
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duración en minutos de cada tramo
*    Calcular el tiempo total de viaje
*    No deben generar errores
"""
try:
    dato_1 = int(input("Ingrese la cantidad de tramos del viaje "))   
    contador= 0
    i = 1
    acum = 0
    while i<= dato_1:
        dato_2 = int(input("Ingrese la duracion del tramo en minutos.  "))
        i += 1
        acum += dato_2

        tiempo_total = acum / 60
except:
    print("ERROR.")    
print(f"El tiempo total de viaje en {dato_1} tramos es de {tiempo_total}")