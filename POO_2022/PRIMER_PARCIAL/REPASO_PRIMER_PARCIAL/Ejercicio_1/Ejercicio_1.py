import clasePila as cp
"""

Utilizando unicamente la clase Pila y sus metodos dados.

-Crear una funcion que me devuelva la cantidad de datos tipo string de una pila.
Importante: La pila al finalizar la funcion tiene que quedar igual.
"""
def contar_string(pila):
    pila_aux = cp.Pila()
    cont= 0
    for i in range(pila.get_tamanio()):
        dato =pila.desapilar()
        if type(dato) == type("str"):
            cont += 1
        pila_aux.apilar(dato)

    for i in range(pila_aux.get_tamanio()):
        pila.apilar(pila_aux.desapilar())

    print(f"Cant string en la pila: {cont}")



pila_1 = cp.Pila()
pila_1.apilar(2)
pila_1.apilar("soy un string")
pila_1.apilar("soy otro string")
pila_1.apilar(5)
pila_1.apilar(6)
pila_1.apilar("yo tmb")
pila_1.ver_pila()
contar_string(pila_1)
pila_1.ver_pila()
