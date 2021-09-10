#19/08/2021
"""
Determinar si una persona tiene fiebre. (fiebre : 37.5 grados) \
    o tiene menos de 30° y sino esta sano
"""

try:
    fiebre = 37.5
    dato_1 = float(input("Ingrese su temperatura "))

    if dato_1 >= fiebre:
        print("Usted tiene fiebre")

    elif dato_1 < 30:
        print("Su temperatura es MUY baja")
    else:
        print("Usted no tiene fiebre")
except:
    print("ERROR.")    
