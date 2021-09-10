#19/08/2021
"""
El programa debe :
*   Almacenar una variable `contraseña` con una contraseña
*   Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por \
     el usuario coincide o no con la variable
 **IMPORTANTE**: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
*   no debe generar errores
"""

try:
    contrasena = "teclado1234"
    dato_1 = str(input("Ingrese la contraseña "))
    if dato_1.lower() == contrasena:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
except:
    print("ERROR.")