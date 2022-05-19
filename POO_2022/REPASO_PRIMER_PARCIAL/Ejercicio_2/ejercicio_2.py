import clasePila as pi
"""
Crear un metodo de pila que elimine los numeros impares que estan apilados
"""
pila_1 = pi.Pila()
pila_1.apilar(2)
pila_1.apilar(3)
pila_1.apilar(4)
pila_1.apilar(5)
pila_1.apilar(6)
pila_1.apilar(7)
pila_1.ver_pila()
pila_1.eliminar_impar()
pila_1.ver_pila()