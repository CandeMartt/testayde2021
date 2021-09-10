#18/08/2021
"""
Agencia de autos:

El programa cuenta con tres marcas de autos y su precio.

El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar
Ford = 10000
Renault = 11000
Chevrolet = 15000
"""
Ford = 10000
Renault = 11000
Chevrolet = 15000
try:
    dinero = float(input("Ingrese la cantidad de dinero que dispone "))
    if dinero >=10000:
        print("Puede comprar un Ford")
    if dinero >=11000:
        print("Puede comprar un Renault")
    if dinero >=15000:
        print("Puede comprar un Chevrolet")
    else:
        print("No puede comprar un auto ya que no dispone de dinero")
except: 
    print("Por favor, ingrese un valor numerico")



