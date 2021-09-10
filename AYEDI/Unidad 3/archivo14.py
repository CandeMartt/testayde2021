#19/08/2021
"""
El programa debe:

-Mostrar al usuario un menu
-Permitir al usuario ingresar una opcion del menu
-imprimir esa opcion
-en caso de no escribir ninuna opcion del menu indicar ERROR
Condiciones:

imprimir (string)
1 (int)
2 (int)
salir (string)
Ayuda (como se comparan string y enteros cuidado con castear antes de verificar \
     si el usuario ingreso str o int)
"""

try:
    dato_1 = (input("""Por favor elija un opcion
    -imprimir
    -1
    -2
    -salir
    Ingreso: """))

    if dato_1.isalpha(): #Para saber si el dato es alfabetico
        if dato_1.lower() == "imprimir":
            print("Usted eligio la opcion: imprimir")
        elif dato_1.lower() == "salir":
            print("Usted eligio la opcion: salir")
        else:
            print("Usted no escribio ninguna de las dos opciones")
    elif dato_1.isdigit(): #Para saber si el dato es numerico
        if int(dato_1) == 1:
            print("Usted eligio la opcion: 1")
        elif int(dato_1) == 2:
            print("Usted eligio la opcion: 2")  
        else:
            print("No ingreso bien el numero")
    else:
        print("Usted no ingresó ninguna de las opciones del menu. Vuelva a intentarlo.") 
except:
    print("ERROR.")
