#01/09/2021
"""
**Ejercicio**
El programa debe:
*   Pedir al usuario una palabra
*   Verificar que sea una palabra y no un numero
*   Mostrar por pantalla las letras una a una
*   No producir errores
"""

while True:
    try:
        palabra = str(input("Por favor ingrese una palabra ")) #no es necesario poner str porque todo entra como str
        if palabra.isalpha():
            for i in palabra:
                print(i)
            break
        else:
            print("Por favor ingrese una palabra sin numeros.")
            
    except:
        ("ERROR.")