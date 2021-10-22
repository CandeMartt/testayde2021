"""
##**Ejercicio 5.5**
Crear una funcion que debe:
*    Tener almacenado el abcedario en una lista
*    Pedir al usuario un numero (2 o 3) - VERIFICAR 
*    Elimina de la lista las letras que ocupen posiciones múltiplos de ese numero
*   Mostrar por pantalla la lista resultante.
*   No deben aparecer y se deben tener en cuenta todos los posibles errores
"""


def multiplos():
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while True:
        numero = input("Por favor ingrese un numero (2 o 3): ")
        if numero == "2" or numero == "3":
            break
        else: 
            print("Por favor ingrese otro numero")
    lista_a_eliminar = []
    for i in range(int(numero), len(lista)+1, int(numero)):
        lista_a_eliminar.append(lista[i-1])   
    
    for i in lista_a_eliminar:
        if i in lista:
            lista.remove(i)

    print(f"El abecedario sin las letras multiplos de {numero} es: \n {lista}")


multiplos()



