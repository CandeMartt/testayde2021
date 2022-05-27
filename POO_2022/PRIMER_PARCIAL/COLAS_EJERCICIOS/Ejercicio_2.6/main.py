#21/04/2022
"""
Utilizando la clase Cola y Pila y sus metodos
-Invertir el contenido de una cola.
"""

import ClaseCola as co
import ClasePila as pi

cola_1 = co.Cola()
cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar(5)
cola_1.encolar(6)
cola_1.encolar(7)
cola_1.encolar(8)
cola_1.ver_cola()

pila_1 = pi.Pila()

for i in range(cola_1.get_tamano()):
    elemento = cola_1.desencolar()
    pila_1.apilar(elemento)

pila_1.ver_pila()

for i in range(pila_1.get_tamanio()):
    elemento = pila_1.desapilar()
    cola_1.encolar(elemento)

cola_1.ver_cola()