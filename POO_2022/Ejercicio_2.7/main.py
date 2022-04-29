#22/04/2022
"""
Utilizando la clase Cola y sus métodos
-Dada una cola de números cargados aleatoriamente, \n
eliminar de ella todos los que no sean primos.
"""
import ClaseColas as co
cola = co.Cola()

while True:
    try:
        numeros = int(input("Ingrese números enteros. Para dejar de agregar valores ponga 000: "))
        if numeros == 000:
            break
        else:
            cola.encolar(numeros)
    except: 
        print("ERROR.")

cola.ver_cola()
cola_aux = co.Cola()


for i in cola.items: #Recorre cada item de la cola
    cont = 0 #el contador debe estar arriba del for que lo vaya usar para que funcione
    #Este segundo for dividira cada elemento por 1, por si mismo y por todos los numeros anteriores a el.
    for j in range(1,i+1): #el +1 ayuda a que se divida por su mismo numero
        if i % j == 0: #Esto nos indica que el numero debe darnos resto cero para que sea divisible
            cont = cont+1 #si da resto 0 lo agrega al contador
    if cont == 2: #nos indica que solo tiene hay dos valores (1 y a si mismo) que dividen al numero 
        print(f"{i} es primo por lo tanto permanecera en la cola.")
        cola_aux.encolar(i)
    else:
        print(f"El numero {i} no es primo, por lo tanto se eliminara de la cola.")
        
cola_aux.ver_cola()
cola_2 = co.Cola()

#volvemos a encolar de nuevo asi nos queda en orden 
for i in range(cola_aux.get_tamano()): #recorro la cola auxiliar
    cola_2.encolar(cola_aux.desencolar()) #lo encolo en una segunda cola para que asi me quede en orden

print("Cola al con los numero NO primos eliminados y ordenada")
cola_2.ver_cola()


