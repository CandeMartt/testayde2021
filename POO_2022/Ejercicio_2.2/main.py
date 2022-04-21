#18/04/2022
"""
###Ejercicio 2.2
Utilizando la clase Pila y sus metodos
*  Permitir que el usuario cargue valores en una Pila
*  Determinar el número de ocurrencias de un determinado elemento en una pila.
"""
import ClasePila as pi
pila_1 = pi.Pila()
pila_aux =pi.Pila()

while True:
    valores = input("Ingrese valores. Para salir escriba: EXIT.")
    if valores == "EXIT":
        break
    else:
        pila_1.apilar(valores)
        pila_aux.apilar(valores)

valores_comparar = input("Ingrese la palabra que quiere comparar: ")
cont_valores = 0
for i in range(pila_aux.get_tamanio()):
    if pila_aux.desapilar() == valores_comparar:
        cont_valores += 1

print(f"La cantidad de vocales es de: {cont_valores}")



