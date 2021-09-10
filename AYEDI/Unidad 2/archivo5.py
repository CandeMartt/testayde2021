#18/08/2021
"""
El programa debe:

-pedir por teclado el dinero actual de una persona
-pedir por teclado el precio del insumo que quiere comprar en USD
-convertir ese dinero a dolares( 1USD -> 170$)
-devoler por pantalla True en caso que pueda comprar, False en caso que no
-No deben aparecer errores
"""

try:
    dinero_actual = float(input("Ingrese su dinero actual(pesos)"))
    precio_insumo = float(input("ingrese el precio del insumo que desea comprar (USD):"))
    dinero_actual_usd = dinero_actual/170
    print(dinero_actual>=precio_insumo)
except:
    print("Error de escritura")