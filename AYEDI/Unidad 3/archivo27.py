"""
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duración en minutos de cada tramo
*    Calcular el tiempo total de viaje
*    No deben generar errores
"""
while True:
    try:
        while True:
            dato_1 = int(input("Ingrese la cantidad de tramos del viaje "))
            if dato_1 <= 0: #detectar si ingreso numeros negativos
                print("Por favor ingrese un numero positivo.")
            else: 
                break

        i = 1
        acum = 0
        for i in range(1,dato_1+1):
            while True:
                dato_2 = int(input(f"Ingrese la duracion del tramo en minutos de {i+1}.  "))
                acum += dato_2 #no se pone i+=1 porque el for itera solo
                tiempo_total = acum / 60
                if dato_2 <= 0: #detectar si ingreso numeros negativos
                    print("Por favor ingrese un numero positivo.")
                else:
                    tiempo_total += dato_2
                    break
        print(f"El tiempo total de viaje en {dato_1} tramos es de {tiempo_total} horas")
        break
    except:
        print("ERROR.")
    
