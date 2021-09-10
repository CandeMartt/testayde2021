#25/08/2021
"""
Ejercicio (Ahora con flag)
El programa debe:
*  pedir un dato al usuario
*  solo en caso que este escriba la palabra clave "python" imprimir por pantalla "Correcto",
 en caso contrario debe seguir pidiendo el dato
*  no deben aparecer errores.
"""

flag = True
while flag:
    try:
        dato_1 = str(input("Ingrese la contraseña "))
        if dato_1.lower() == "python":
            print("La contraseña es correcta")
            flag = False
    except:
        print("ERROR.")

