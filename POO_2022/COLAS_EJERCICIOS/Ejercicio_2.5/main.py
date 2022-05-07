#21/04/2022
"""
Utilizando la clase Cola y sus metodos
-Eliminar el i-ésimo elemento después del frente de la cola.
"""

import ClaseCola as co
cola_1 = co.Cola()

cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar(5)
cola_1.encolar(6)
cola_1.encolar(7)
cola_1.encolar(8)
cola_1.ver_cola()

while True:
    try:
        numero = int(input("Ingrese el numero de elemento de la cola a eliminar(no puede ser el primero): "))
    except:
        print("ERROR.")
    if (numero <= 1 or numero> cola_1.get_tamano()):
        print("No puede ser el 1º valor o el numero es mas grande que la cola")
    else:
        break
for i in range(cola_1.get_tamano()):
    if i == numero-1:
        print(f"Se elimino el elemento: {cola_1.desencolar()} ")
        
    else:
        cola_1.mover_al_final()

cola_1.ver_cola()