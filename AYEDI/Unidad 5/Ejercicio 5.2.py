"""
##**Ejercicio 5.2**
Crear una funcion que debe:

*    Pedir al usuario una palabra o una frase
*    Indicar si esta se trata de un palindromo (reconocer, neuquen, amor a roma)
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

palabra_frase = str(input("Ingrese una palabra o una frase: "))

lista = ["reconocer", "neuquen", "amor a roma"]
for i in palabra_frase:
    if palabra_frase in lista:
            print(f"La palabra o frase {palabra_frase} que usted ingreso es palindromo.")
            break
else:
    print("La palabra no es un palindromo")