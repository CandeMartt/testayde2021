import claseCola as co
"""
Utilizando unicamente la clase Cola y sus metodos dados 
(si es necesario tmb se puede utilizar la clase PILA).

-Crear una funcion que me devuelva la cantidad de datos tipo int de una cola.
Importante: La cola al finalizar la funcion tiene que quedar igual.
"""
def contar_int(cola):
    cola_aux = co.Cola()
    cont = 0
    while cola.es_vacia() == False:
        dato = cola.desencolar()
        if type(dato) == type(1):
            cont += 1
        cola_aux.encolar(dato)
    
    while cola.es_vacia() == False:
        cola.encolar(cola_aux.desencolar())

    print(f"Cant int en la cola: {cont}")


cola_1 = co.Cola()
cola_1.encolar(2)
cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar(5)
cola_1.encolar(6)
cola_1.encolar(7)
cola_1.encolar(8)
cola_1.ver_cola()
contar_int(cola_1)
cola_1.ver_cola()